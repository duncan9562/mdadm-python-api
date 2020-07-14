import mdstat
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Homepage</h1>'''

@app.route('/api/v1/resources/mdadm/md0', methods=['GET'])
def api_all():
    status = mdstat.parse()
    return jsonify(status)

app.run(host='0.0.0.0')
