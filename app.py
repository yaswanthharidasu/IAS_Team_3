from flask import Flask, request
import sensor_manager
import mongo

app = Flask(__name__)

@app.route("/registerSensorType", methods=["POST"])
def registerSensorType():
    sensor_type = request.json
    sensor_manager.registerSensorType(sensor_type)
    return "Registered Sensor Type successfully"


@app.route("/registerSensorInstance", methods=["POST"])
def registerSensorInstance():
    sensor_instance = request.json
    sensor_manager.registerSensorInstance(sensor_instance)
    return "Registered Sensor Instance successfully"


@app.route("/getSensorData", methods=["GET"])
def getSensorData():
    return "Hello"


if __name__ == "__main__":
    # Initializing the database
    # mongo.create_database()
    app.run(port=5000, debug=True)