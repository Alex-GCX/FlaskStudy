from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def show_response():
    # 1.使用元组,返回自定义响应信息(响应体, 状态码, 响应头)
    # return ('index page', 400, [('name', 'python'), ('city', 'beijing')])
    # return ('index page2', 400, {'name': 'python2', 'city': 'beijing2'})
    # return ('index page3', '600 customize status', {'name': 'python3',
                                                    #  'city':'beijing3'})
    # 2.使用make_response来构造响应信息
    resp = make_response('首页')  # 响应体
    resp.status = '600 customize status' # 状态码
    resp.headers['city'] = 'beijing4'
    return resp
