from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# 配置邮箱
app.config.update(
    DEBUG = True,
    MAIL_SERVER='smtp.163.com',
    MAIL_PROT=25,
    # MAIL_USE_TLS = True,
    MAIL_USERNAME = 'g1242556827@163.com',
    MAIL_PASSWORD = 'ENYWOVQSLWHGIUEX',
)

mail = Mail(app)

@app.route('/')
def index():
    # 发送方,接收方
    msg = Message(
        'this is a test', sender='g1242556827@163.com',
        recipients=['1242556827@qq.com']
    )
    # 邮件内容
    msg.body = 'Flask test mail'
    # 发送邮件
    mail.send(msg)
    return 'send success'

