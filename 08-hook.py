from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/index')
def index():
    print('index run')
    a = 1 / 0
    return 'index page'


@app.route('/hello')
def hello():
    print('hello run')
    return 'hello page'


@app.before_first_request
def before_first_request():
    print('应用启动后第一个请求会被执行, 在视图函数执行前执行')


@app.before_request
def before_request():
    print('每次请求进来时都会被执行, 在视图函数执行前执行')
    # 每个钩子函数在个视图函数中都会被执行
    # 如果需要在一个钩子函数中对于不同的视图函数执行不同的逻辑
    # 当前url地址可以通过request对象获取，视图函数的url地址可以通过url_for来反向解析获取到
    if request.path == url_for('index'):
        print('这是只在index页面单独做的操作')
    elif request.path == url_for('hello'):
        print('这是只在hello页面单独做的操作')


@app.after_request
def after_request(response):
    print('每次请求结束时都会被执行， 在视图函数执行后执行, 且视图函数没有发生异常(测试发现视图函数发生异常了也会执行)')
    return response


@app.teardown_request
def teardown_request(response):
    print('每次请求结束时都会被执行， 在after_request钩子函数执行后执行，且无论视图函数是否发生异常，但需要关闭DEBUG模式才能看到效果')
    return response
