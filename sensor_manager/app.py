from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from itsdangerous import json
import sensor_manager
import mongo
import kafka_manager

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


################################## SENSOR REGISTRATION ########################################

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


################################# GET A SENSOR DATA ###########################################

@app.route("/getSensorData", methods=["POST"])
def getSensorData():
    topic_name = request.json['topic_name']
    sensor_data = sensor_manager.getSensorData(topic_name)
    return jsonify(sensor_data)


################################ GET SENSOR DETAILS USING LOCATION #############################

@app.route("/getSensorTypes", methods=["POST"])
def getSensorTypes():
    location = request.json['location']
    sensor_types = sensor_manager.getSensorTypes(location)
    return jsonify(sensor_types)


@app.route("/getSensorInstances", methods=["POST"])
def getSensorInstances():
    sensor_type = request.json['sensor_type']
    location = request.json['location']
    sensor_instances = sensor_manager.getSensorInstances(sensor_type, location)
    return jsonify(sensor_instances)


############################### GET ALL SENSOR DETAILS #############################################

@app.route("/getAllSensorTypes", methods=["GET"])
def getAllSensorTypes():
    sensor_types = sensor_manager.getAllSensorTypes()
    return jsonify(sensor_types)


@app.route("/getAllSensorInstances", methods=["GET"])
def getAllSensorInstances():
    sensor_instances = sensor_manager.getAllSensorInstances()
    return jsonify(sensor_instances)


################################### MAIN #############################################################

if __name__ == "__main__":
    if mongo.databaseExists() == False:
        print("DATABASE CREATED...")
        sensor_manager.register_sensors_from_json("sensor_config.json")
    else:
        print("DATABASE ALREADY EXISTS...")
        kafka_manager.produce_sensors_data()

    app.run(port=5000, debug=True)
