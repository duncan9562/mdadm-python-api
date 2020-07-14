import mdstat
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Homepage</h1>'''

@app.route('/api/v1/resources/mdadm/md0/non_degraded_disks', methods=['GET'])
def api_all():
    status = mdstat.parse()
    return status['devices']['md0']['status']['non_degraded_disks']

app.run(host='0.0.0.0')
