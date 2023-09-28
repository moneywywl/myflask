import json

from flask import Flask, request, abort, g
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def authLogin(func):
    def authPassword(*args, **kwargs):
        if g.password != "123":
            return {"msg:": "err", "data": "密码校验错误！"}, 401
        else:
            print("sddsad",*args, **kwargs)
            return func(*args, **kwargs)

    return authPassword


@app.before_request
def login():
    g.password = None
    if request.json["userName"] != '123':
        return {"msg": "err", "data": "用户名校验错误！"}, 401
    else:
        if "password" in request.json:
            g.password = request.json["password"]



class UpdateOrder(Resource):
    @authLogin
    def post(self):
        print(request.json)
        return {"msg": "ok", "sqlTxt": json.loads(request.data)["sqlText"]}


api.add_resource(UpdateOrder, "/UpdateOrder")

if __name__ == "__main__":
    app.run(debug=True)
