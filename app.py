from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from itsdangerous import json
import sensor_manager
import mongo
import kafka_manager

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/registerSensorType", methods=["POST"])
def registerSensorType():
    sensor_type = request.json
    sensor_manager.registerSensorType(sensor_type)
    return json.dumps({"data": "Registered Sensor Type successfully"})


@app.route("/registerSensorInstance", methods=["POST"])
def registerSensorInstance():
    sensor_instance = request.json
    sensor_manager.registerSensorInstance(sensor_instance)
    return json.dumps({"data": "Registered Sensor Instance successfully"})


@app.route("/getSensorData", methods=["POST"])
def getSensorData():
    sensor_data = sensor_manager.getSensorData
    return sensor_data


@app.route("/getSensorDetails", methods=["POST"])
def getSensorDetails():
    location = request.json['location']
    sensor_details = jsonify(sensor_manager.getSensorDetails(location))
    return sensor_details

if __name__ == "__main__":
    mongo.checkDatabase()
    kafka_manager.produce_sensors_data()
    app.run(port=5000, debug=True)
