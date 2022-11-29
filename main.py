from flask import Flask
from flask_restful import Api, Resource, reqparse

# create app
app = Flask(__name__)
# wrap app in a restful API
api = Api(app)

video_put_args = reqparse.RequestParser()

Videos = {}

# handle get, pull, delete requests
class Video(Resource):
    def get(self, video_id):
        return Videos[video_id]

    def put(self, video_id):
        print(requests.form)
        return {}
        

# when https ends with /helloworld, send get request
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
