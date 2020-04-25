from flask import Flask, json
from flask_cors import CORS, cross_origin

app = Flask(__name__) 
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def home_view(): 
        return "<h1>Hello world</h1>"

@app.route('/fetch/name', methods=['GET'])
@cross_origin()
def get_bucket():
        return app.response_class(
                response=json.dumps({"result": "Hello world from api call."}),
                status=200,
                mimetype="application/json")