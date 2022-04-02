from urllib import response
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from itsdangerous import json
import control_db
import control_manager
import requests

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


################################## SENSOR REGISTRATION ########################################

@app.route("/performAction", methods=["GET", "POST"])
def performAction():
    instance = request.json
    print(instance)
    # sensor_type = instance["sensor_type"]
    url = "http://localhost:"
    if instance["sensor_type"] == "fan":
        url += str(7000) + "/fanAction"
    elif instance["sensor_type"] == "ac":
        url += str(7001) + "/acAction"
    
    response = requests.post(url, json={
        "data": 0
    }).content
    print(response.decode())
    return response.decode()

################################### MAIN #############################################################

if __name__ == "__main__":
    if control_db.databaseExists() == False:
        print("DATABASE CREATED...")
        control_manager.register_controllers_from_json("control_config.json")
    
    app.run(port=5000, debug=True)
