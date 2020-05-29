from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    print('data:', request.data)
    print('args:', request.args['id'])
    return 'index page'
