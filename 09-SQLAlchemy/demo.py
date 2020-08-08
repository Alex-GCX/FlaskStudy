from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 创建Flask应用
app = Flask(__name__)

# 配置数据库连接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@47.102.114.90:3306/sqlalchemy_test'
# 创建数据库实例
db = SQLAlchemy(app)
# 创建数据库迁移对象
migrate = Migrate(app, db)


# 定义角色类, 继承db.Model类
class Role(db.Model):
    # 手动定义表名, 否则默认为小写的类名
    __tablename__ = 'test_roles'
    # 定义字段, 格式为: 字段名 = db.Column(db.类型, 附加属性[主键/唯一性等])
    id = db.Column(db.Integer, primary_key=True)  # 主键必须显示定义出来
    name = db.Column(db.String(20), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Role {self.name}>'


# 定义用户类, 继承db.Model类
class User(db.Model):
    # 手动定义表名, 否则默认为小写的类名
    __tablename__ = 'test_users'
    # 定义字段, 格式为: 字段名 = db.Column(db.类型, 附加属性[主键/唯一性等])
    id = db.Column(db.Integer, primary_key=True)  # 主键必须显示定义出来
    name = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(30), unique=True)
    # 注意定义ForeignKey的时候, 参数为'数据库表名_字段名', 而不是'类名_字段名'
    role_id = db.Column(db.Integer, db.ForeignKey('test_roles.id'))
    # 建立两个模型类的逻辑连接关系
    role = db.relationship('Role', backref='user')

    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role

    def __repr__(self):
        return f'<User {self.name}>'
