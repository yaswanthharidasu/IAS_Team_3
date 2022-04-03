import csv
import requests
import api
import json
import sleep


# data_file = open('application.json')
# data = json.load(data_file)
# sd = data['sensor']

while(1):
    data = api.getSensorData()
    prediction = api.predict(data)
    output = api.controllerAction(prediction[0])
    print(output)
    sleep(60)
