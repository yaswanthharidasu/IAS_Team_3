from urllib import response
import requests

def getData(topic_name):
    response = requests.post("http://localhost:5000/getSensorData", data={
        "topic_name": topic_name
    })
    print(response.json)

getData()