from urllib import response
from itsdangerous import json
import requests
import json
import random

def getSensorTopics(sensor_type, location):
    response = requests.post(url='http://localhost:5000/getSensorInstances', json={
        "sensor_type": sensor_type,
        "sensor_location": location
    }).content
    sensor_instances = json.loads(response.decode())
    return sensor_instances
    
def getSensorData(sensor_type, location, count_instances):
    all_instances = getSensorTopics(sensor_type, location)
    sensor_instances = random.sample(all_instances, count_instances)    
    response = requests.post(url='http://localhost:5000/getSensorData', json={
        "topic_name": sensor_instances[0]
    }).content
    
getSensorData("light", "himalaya-block")