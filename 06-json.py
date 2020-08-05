from flask import Flask, json,  jsonify, Response

app = Flask(__name__)

@app.route('/')
def show_json():
    # json就是字符串,写法类似字典
    data = {
        'name': 'python',
        'age': '12'
    }
    # 1.使用json模块
    # json.dumps(字典) 将dict转换为json字符串
    # json.loads(字符串) 将字符串转换为dict
    # json_str = json.dumps(data)
    # return json_str, 200, {"Content-Type": "application/json"}

    # 2.使用jsonify
    # jsonify可以将dict转换为字符串并返回一个response对象,
    # 并且设置响应头的 Content-Type 为application/json
    print(type(Response('aaaaa')))  # <class 'flask.wrappers.Response'>
    print(type(jsonify(data)))  # <class 'flask.wrappers.Response'>
    # 方式一
    return jsonify(data)
    # 方式二
    # return jsonify(city="shanghai", country="CN")
