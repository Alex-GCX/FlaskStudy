from flask import Flask, abort, Response

app = Flask(__name__)

@app.route('/')
def show_abort():
    # abort可以立即终止视图函数,并可以返回指定的信息给前端
    # 1.返回状态码,必须时标准的http状态码
    abort(404)
    # 2.返回Response对象
    #  resp = Response('......error1.....')
    #  abort(resp)
    # return resp  # return也可以返回Response对象
    # return 'Index'

# 自定义标准错误状态码的处理方法
@app.errorhandler(404)
def handle_404_error(err):
    return '返回自定义错误信息,出现了404错误,错误信息为:%s' % err
