from flask import Flask

# __name__表示当前模块的名字
# 创建Flask对象,接收一个参数,用来指定模块名
app = Flask(__name__,  # 模块名,flask以这个模块所在的目录为总目录
            static_url_path='/static',  # 访问静态资源的url前缀,默认值是static
            static_folder='static',  # 服务器目录中的静态文件目录,默认就是static
            template_folder='templates',  # 服务器目录中的模板文件的目录,默认就是templates
           )

# 二.配置项目参数的使用,即django中setting.py
# 1. 使用目录中的,配置文件
# app.config.from_pyfile('config.cfg')

# 2. 使用对象配置
class Config:
    DEBUG = False
    MY_CONFIG = 'python'

app.config.from_object(Config)

# 3.直接操作config的字典对象
#  app.config['DEBUG'] = True
#  app.config['MY_CONFIG'] = 'python'

# 装饰器用来将路由映射到视图函数hello_world中
@app.route('/')
def hello_world():
    # 通过app.config.get获取配置的值
    return 'hello world! ' + app.config.get('MY_CONFIG')

if __name__ == '__main__':
    # 启动flask程序
    # app.run()
    app.run(host='0.0.0.0', port=5000, debug=True)
