import requests
import json
import random

sensor_url = 'http://localhost:5000/'
control_url = 'http://localhost:6000/'
model_url = 'http://localhost:5003/'
model_name = "ac_prediction_model"


def readFromFile(path, key):
    f = open(path, 'r')
    data = json.load(f)
    if key == "sensor_details":
        data = data["sensor_details"]
        return data['sensor_type'], data['sensor_location'], data['no_of_instances']
    elif key == "controller_details":
        data = data["controller_details"]
        return data['sensor_type'], data['sensor_location']


def getSensorInstances(path="app_configuration.json"):
    sensor_type, sensor_location, no_of_instances = readFromFile(
        path, "sensor_details")
    url = sensor_url+'getSensorInstances'
    response = requests.post(url=url, json={
        "sensor_type": sensor_type[0],
        "sensor_location": sensor_location
    }).content
    data = json.loads(response.decode())
    sensor_instances = data["sensor_instances"]
    return sensor_instances, no_of_instances


def getControlInstances(path="app_configuration.json"):
    sensor_type, sensor_location = readFromFile(path, "controller_details")
    url = control_url+'getControlInstances'
    response = requests.post(url=url, json={
        "sensor_type": sensor_type,
        "sensor_location": sensor_location
    }).content
    data = json.loads(response.decode())
    control_instances = data['control_instances']
    return control_instances


def getSensorData():
    all_instances, no_of_instances = getSensorInstances()
    sensor_instances = random.sample(all_instances, no_of_instances)
    url = sensor_url+'getSensorData'
    response = requests.post(url=url, json={
        "topic_name": sensor_instances[0]
    }).content
    data = json.loads(response.decode())
    data = data['sensor_data']
    return data[-1]


def controllerAction(data):
    all_instances = getControlInstances()
    instance = all_instances[0]
    url = control_url+'performAction'
    response = requests.post(url=url, json={
        "sensor_type": instance["sensor_type"],
        "sensor_ip": instance["sensor_ip"],
        "sensor_port": instance["sensor_port"],
        "data": int(data)
    }).content
    return response.decode()


def predict(data):
    # MAKE API call to the model
    url = model_url+'predict'
    response = requests.post(url=url, json={
        "data": data.tolist(),
        "model_name": model_name
    }).content
    prediction = json.loads(response.decode())
    prediction = prediction["predicted_value"]
    return prediction


# getSensorData("light", "himalaya-block")
# readFromFile()
