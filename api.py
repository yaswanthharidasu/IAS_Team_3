from urllib import response
from itsdangerous import json
import requests
import json
import random
import numpy as np
import pickle

def readFromFile(path, key):
    f = open(path, 'r')
    data = json.load(f)
    if key == "sensor_details":
        data = data["sensor_details"]
        return data['sensor_type'], data['location'], data['no_of_instances']
    elif key == "controller_details":
        data = data["controller_details"]
        return data['sensor_type'], data['location']


def getSensorTopics(path="app_configuration.json"):
    sensor_type, sensor_location, no_of_instances = readFromFile(
        path, "sensor_details")
    response = requests.post(url='http://localhost:5000/getSensorInstances', json={
        "sensor_type": sensor_type[0],
        "sensor_location": sensor_location
    }).content
    sensor_instances = json.loads(response.decode())
    return sensor_instances, no_of_instances


def getControllerDetails(path="app_configuration.json"):
    sensor_type, sensor_location = readFromFile(path, "controller_details")
    response = requests.post(url='http://localhost:6000/getControlInstances', json={
        "sensor_type": sensor_type,
        "sensor_location": sensor_location
    }).content
    control_instances = json.loads(response.decode())
    return control_instances


def getSensorData():
    all_instances, no_of_instances = getSensorTopics()
    sensor_instances = random.sample(all_instances, no_of_instances)
    response = requests.post(url='http://localhost:5000/getSensorData', json={
        "topic_name": sensor_instances[0]
    }).content
    # print(response.decode())
    data = response.decode()
    data = json.loads(data)
    data = data['sensor_data']
    return data[-1]


def controllerAction(data):
    all_instances = getControllerDetails()
    instance = all_instances[0]
    url = 'http://'+instance["sensor_ip"]+":"+instance["sensor_port"]
    if instance["sensor_type"] == "fan":
        url += "/fanAction"
    elif instance["sensor_type"] == "ac":
        url += "/acAction"
    # print(data, url)
    response = requests.post(url=url, json={
        "data": int(data)
    }).content
    return response.decode()

def predict(data):
    # MAKE API call to the model
    data = np.reshape(np.array(data), (-1, 1))
    model_file = open('gen_model.pkl', 'rb')
    load_model = pickle.load(model_file)
    predictions = load_model.predict(data)
    return predictions
    

# getSensorData("light", "himalaya-block")
# readFromFile()
