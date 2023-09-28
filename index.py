from flask import Flask, Blueprint, request
from werkzeug.routing import BaseConverter
from user import user_bp

app = Flask(__name__)
app_bp = Blueprint("user", __name__)


class PhoneNumConverter(BaseConverter):
    regex = r"1[3-9]\d{9}"


app.url_map.converters["phoneNum"] = PhoneNumConverter


@app.route("/<phoneNum:user_name>")
def index(user_name):
    return f"hello word!{user_name}"


@app.route("/test")
def test():
    userName = request.args.get("userName")
    return f"学生姓名：{userName},请求方法为：{request.method},请求头：{request.headers.get('sec-ch-ua-platform')}，请求体：{request.data},cookie：{request.cookies}"


@app.route("/upFile", methods=["POST"])
def upFile():
    f = request.files["file"]
    print(f.content_type)
    f.save(f"./{f.filename}")
    return "OK"


app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(debug=True,port=5000,host='0.0.0.0')
