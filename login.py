import datetime
from flask import Flask, make_response, request, session, abort
import json

app = Flask(__name__)
app.secret_key = "ASDS123SSD1123"
app.permanent = True
app.permanent_session_lifetime = datetime.timedelta(hours=10)


@app.route("/", methods=["POST"])
def login():
    rawRquest = json.loads(request.data)
    print()
    if rawRquest["userName"] == '黄蕾':
        reqs = make_response(f"尊贵的VIP：{rawRquest['userName']},欢迎您登录!")
        reqs.set_cookie("userid", '7122333')
        reqs.status = "400 is ok"
        session[rawRquest["uuid"]] = '7122333'

        return reqs
    else:
        return "登录失败！"


@app.route("/getSession", methods=["POST"])
def getSession():
    return "sddsa"
    # rawRquest = json.loads(request.data)
    # if rawRquest["uuid"] in session.keys():
    #     return session.get(rawRquest["uuid"])
    # else:
    #     abort(500)


@app.errorhandler(500)
def testErr(e):
    return "登录错误！！！！！！"


@app.before_request
def BeforgetSession():
    rawRquest = json.loads(request.data)
    if rawRquest["uuid"] in session.keys():
        return session.get(rawRquest["uuid"])
    else:
        abort(500)


if __name__ == "__main__":
    app.run(debug=True)
