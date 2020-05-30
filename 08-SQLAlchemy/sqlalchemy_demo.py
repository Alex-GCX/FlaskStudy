from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/flask_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 创建数据库对象
db = SQLAlchemy(app)
# 创建数据库迁移对象
migrate = Migrate(app, db)

# 创建数据表对应的类
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rolename = db.Column(db.String(80), unique=True)
    user = db.relationship('User', backref='role', lazy='dynamic')

    #  def __init__(self, rolename):
        #  self.rolename = rolename

    def __repr__(self):
        return '<Role %r>' % self.rolename


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(90), unique=True)
    email = db.Column(db.String(120), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    #  def __init__(self, username, email):
        #  self.username = username
        #  self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

if __name__ == '__main__':
    admin = Role(rolename='admin')
    staff = Role(rolename='staff')

    # 插入数据
    python = User(username='python', email='python@123.com', role=admin)
    zhao = User(username='zhao', email='zhao@123.com', role=staff)
    qian = User(username='qian', email='qian@123.com', role=staff)
    sun = User(username='sun', email='sun@123.com', role=staff)
    li = User(username='li', email='li@123.com', role=staff)
    db.session.add_all([python, zhao, qian, sun, li])
    db.session.commit()
