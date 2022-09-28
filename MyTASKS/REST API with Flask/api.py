from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {
    "Qosim":{"age":21,"gender": "male"},
    "Nasim":{"age":20,"gender": "male"},
    "Zuhal":{"age":20,"gender": "women"}
}

class HelloWorld(Resource):
    def get(self,name):
        return names[name]
    def post(self):
        return {"data": "Hellow world"}

api.add_resource(HelloWorld,"/helloworld/<string:name>")


if __name__ == "__main__":
    app.run(debug=True)

