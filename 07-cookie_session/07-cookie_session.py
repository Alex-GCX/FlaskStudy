from flask import Flask, request, redirect, url_for, render_template, session
from flask import make_response, flash

app = Flask(__name__)

# 设置密钥
app.secret_key = 'awnawu31231n231jnajnw'

# 使用session实现记录登录状态
# 使用cookie实现记录登录页面的登录名,和密码

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # 获取cookie
        name = request.cookies.get('name', '')
        pwd = request.cookies.get('pwd', '')
        return render_template('login.html', name=name, pwd=pwd)
    # 获取表单数据
    name = request.form.get('name')
    pwd = request.form.get('pwd')

    if (name == 'python' and pwd == '123') or (name == '123' and pwd == '123'):
        # 登录成功
        # 设置登录成功的session
        # flask默认把session保存到了cookie中
        session['name'] = name
        # 使用cookie记录用户名
        resp = make_response(redirect(url_for('index')))
        resp.set_cookie('name', name)
        resp.set_cookie('pwd', pwd)
        return resp
    errmsg = '用户名密码错误'
    flash(errmsg)
    # 使用cookie记录用户名
    resp = make_response(redirect(url_for('login')))
    resp.set_cookie('name', name)
    resp.set_cookie('pwd', pwd)
    return resp


@app.route('/index')
def index():
    # 获取登录session
    if 'name' in session:
        name = session['name']
        return render_template('index.html', name=name)
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    # 删除session信息
    # 因为flask是将session存到了浏览器的cookie中,所以这里删除session信息时
    # 并非删除浏览器中的cookie,而是将该cookie的到期时间设置为其创建时间,即使cookie失效
    session.pop('name', None)
    # 重定向到登录页面
    return redirect(url_for('login'))
