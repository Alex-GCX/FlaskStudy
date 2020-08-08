from flask import Flask, request, abort, render_template
import hashlib
import xmltodict
import time
import json
import urllib.request as urllib2

app = Flask(__name__)
WECHAT_TOKEN = 'python'
WECHAT_APPID = 'wx3b89dbc4edc24f1e'
WECHAT_APPSECRET = '9e410c7f56a2f43e4849875cfc271208'

@app.route('/wechat', methods=['GET', 'POST'])
def connect_wechat():
    # 微信每次请求服务器时,都会在URL中传入下面三个参数
    # 1. 校验请求是否是微信服务器发送过来的
    # 获取参数
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    # 校验参数
    if not all([signature, timestamp, nonce]):
        abort(400)
    # 排序
    temp = [WECHAT_TOKEN, timestamp, nonce]
    temp.sort()
    # 拼接
    temp = ''.join(temp)
    # sha1加密
    sha1 = hashlib.sha1(temp.encode('utf-8')).hexdigest()
    if sha1 != signature:
        # 秘钥不匹配
        abort(403)

    # 2. 秘钥正确,处理业务逻辑
    if request.method == 'GET':
        # GET请求说明是第一次接入微信
        echostr = request.args.get('echostr')
        if echostr:
            return echostr
        abort(400)

    # 否则为POST请求,说明是微信转发过来的XML消息
    #  <xml>
    #  <ToUserName><![CDATA[gh_866835093fea]]></ToUserName>
    #  <FromUserName><![CDATA[ogdotwSc_MmEEsJs9-ABZ1QL_4r4]]></FromUserName>
    #  <CreateTime>1478317060</CreateTime>
    #  <MsgType><![CDATA[text]]></MsgType>
    #  <Content><![CDATA[你好]]></Content>
    #  <MsgId>6349323426230210995</MsgId>
    #  </xml>
    # 获取xml
    rcv_xml_str = request.data
    print('rcv_xml_str:\n', rcv_xml_str)
    if not rcv_xml_str:
        abort(400)
    # 将xml转化为字典
    rcv_xml_dict = xmltodict.parse(rcv_xml_str)
    rcv_xml_dict = rcv_xml_dict.get('xml')
    # 获取具体的消息
    msg_type = rcv_xml_dict.get('MsgType')
    # 需求,如果是text消息则返回原消息,否则返回'请输入文本格式的消息'
    if msg_type == 'text':
        content = rcv_xml_dict.get('Content')
    # 如果返回的是事件且是关注的话,返回感谢关注
    elif msg_type == 'event' and rcv_xml_dict.get('Event')=='subscribe':
        msg_type = 'text'
        content = '感谢你的关注'
    else:
        msg_type = 'text'
        content = '请输入文本格式的消息'
    # 构造返回的消息
    send_xml_dict = {'ToUserName': rcv_xml_dict.get('FromUserName'),
                     'FromUserName': rcv_xml_dict.get('ToUserName'),
                     'CreateTime': int(time.time()),
                     'MsgType': msg_type,
                     'Content': content
                    }
    # 字典转换为XML
    send_xml_str = xmltodict.unparse({'xml': send_xml_dict}).encode('utf-8')
    print('send_xml_str:\n', send_xml_str)
    return send_xml_str


@app.route('/wechat/index')
def index():
    """让用户通过微信浏览器访问的网址"""
    # 从微信服务器中拿用户资料
    code = request.args.get('code')
    if not code:
        abort(400)

    # 向微信获取access_token
    url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code' % (WECHAT_APPID, WECHAT_APPSECRET, code)
    # 使用urllib2发送请求,默认使用GET
    resp = urllib2.urlopen(url)
    # 获取响应的json数据
    resp_json = resp.read()
    # 将json转换为字典
    resp_dict = json.loads(resp_json)
    # 判断响应中是否有错
    if 'errcode' in resp_dict:
        return '获取access_token失败:%s' % resp_dict['errcode']
    # 提取access_token
    access_token = resp_dict.get('access_token')
    open_id = resp_dict.get('openid')

    # 再向微信服务器发送请求,获取用户数据
    url = "https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s&lang=zh_CN" % (access_token, open_id)
    resp = urllib2.urlopen(url)
    # 获取响应json
    user_json_data = resp.read()
    # 转为字典
    user_dict_data = json.loads(resp_json)
    # 判断响应是否有错
    if 'errcode' in resp_dict:
        return '获取用户数据失败:%s' % resp_dict['errcode']

    return render_template('index.html', user=user_dict_data)
