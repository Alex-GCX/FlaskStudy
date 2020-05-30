from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # 获取请求方式
    print('method: ', request.method)
    # form和data是用来提取请求体body数据

    # form提取的是表单格式的数据,返回一个类字典的对象
    # 表单格式的数据如:id=xxx&name=xxx&age=xxx
    print('form: ', request.form)
    print('form_id: ', request.form.get('form_id'))
    print('form_name: ', request.form.get('form_name'))

    # get只能拿到多个同名参数的第一个,若要获取多个,通过getlist()获取
    print('city: ', request.form.getlist('city'))

    # data提取的是除了表单格式之外的数据(如json格式),也是返回一个类字典的对象
    print('data: ', request.data)

    # args获取的是url中的?参数
    print('args: ', request.args)
    print('args_id: ', request.args.get('args_id'))
    print('args_name: ', request.args.get('args_name'))

    # cookies:获取请求中的cookie信息,Dict
    print('cookies: ', request.cookies.get('xxx'))
    # headers:获取请求报文头
    print('headers: ', request.headers)
    # url:获取请求的url, string
    print('url: ', request.url)

    # files:获取请求上传的文件
    # 获取传递的文件对象
    file_ojb = request.files.get('pic')
    if not file_ojb:
        return '未上传文件'
    # 读取文件
    file_ojb.save('./demo.png')
    return 'upload sucess'
