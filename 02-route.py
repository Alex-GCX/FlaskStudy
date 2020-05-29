from flask import Flask, redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

# 限制只能用POST访问
@app.route('/hello', methods=['POST'])
def hello():
    return 'Hello'

# 一个路由下有多个视图函数, 则只会对应第一个定义的视图函数
@app.route('/one')
def show_one1():
    return 'one1'

@app.route('/one')
def show_one2():
    return 'one2'

# 多个路由对一个视图函数进行装饰
@app.route('/hello1')
@app.route('/hello2')
def hello1():
    return 'hello1'

# 使用redirct重定向, url_for进行反向解析
@app.route('/login')
def login():
    return 'start login'

@app.route('/index')
def get_index():
    url = url_for('login')
    return redirect(url)

# 路由中的变量规则
@app.route('/user/<username>')
def show_user_profile(username):
    return 'User is %s' % username
# 路由转换器
#  string:（缺省值） 接受任何不包含斜杠的文本
#  int:接受正整数
#  float:接受正浮点数
#  path:类似 string ，但可以包含斜杠
#  uuid:接受 UUID 字符串
@app.route('/center/<int:userid>')
def show_user(userid):
    return 'userid is %d' % userid

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'subpath is %s' % subpath

# 自定义转换器
# 1.定义转换器类,必须继承BaseConverter
class RegexConverter(BaseConverter):
    """自定义转换器类"""
    def __init__(self, url_map, regex):
        # 调用父类初始化方法
        super().__init__(url_map)
        # 将正则表达式参数保存到对象的固定属性regex中，属性名不可变
        self.regex = regex

    # 只定义__init__方法即可完成基本的转换器功能
    # 下面两个函数能够实现更加高级的功能
    def to_python(self, value):
        """
        当调用视图函数,将url中转换器后面的路由变量(phone)传给视图函数之前
        会自动调用to_python方法，该方法可以对路由变量进行进一步的操作，如其他校验之类的逻辑
        操作完之后，将结果返回，即该函数的返回值才是传给视图函数的参数值
        父类中该方法默认直接返回路由变量的值
        """
        print('to_python被调用')
        return 'abc'  # 手动修改返回值，则视图函数接受到的参数值即为abc

    def to_url(self, value):
        """
        当url_for进行反向解析前，会自动调用to_url方法，对路由变量进行进一步操作
        操作完之后，将结果返回给解析后的url，即该函数的返回值才是最终反向解析后的url变量的值
        父类中该方法默认直接返回路由变量的值
        """
        print('to_url被调用')
        return '13111111111'  # 手动修改返回值，则url拼上的参数值即为13111111111

# 2.将定义的转换器添加到flask应用中
app.url_map.converters['re'] = RegexConverter
# 3.使用转换器
@app.route("/convert/<re(r'1[3578]\d{9}'):phone>")
def show_phone(phone):
    return 'phone is %s' % phone # 最终结果为 phone is abc

@app.route('/convert/redict')
def redict_phone():
    """重定向到上面的/convert/15100000000中"""
    # 使用url_for反向解析时，当需要给url路由变量赋值时，需要以**kwargs的形式赋值
    url = url_for('show_phone', phone='15100000000')
    return redirect(url) # 最终重定向的地址为/convert/13111111111
# print(app.url_map)
