import json
from sys import api_version
import pymongo
import threading
import sensor_data
from pydoc import doc

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["SensorDatabase"]
instancesdb = mydb["SensorInstances"]
# types = mydb["SensorTypes"]

# Deprecated
# def register_sensor_type(sensor_type):
#     types = mydb["SensorTypes"]
#     types.insert_one(sensor_type)


def checkDatabase():
    databases = client.list_database_names()
    if 'SensorDatabase' not in databases:
        register_sensors_from_json('sensor_config.json')


def register_sensor_instance(sensor_instance):
    '''Stores the given sensor_instance in the collection'''
    count = getCount(instancesdb)
    sensor_instance['_id'] = count+1
    instancesdb.insert_one(sensor_instance)


def register_sensors_from_json(path):
    f = open(path)
    sensors = json.load(f)
    for instance in sensors['sensor_instances']:
        register_sensor_instance(instance)


def drop_db():
    instancesdb.drop()
    client.drop_database("SensorDatabase")


def getCount(collectionObj):
    '''Returns no.of documents in the given collection object'''
    return collectionObj.count_documents({})


def get_sensor_types():
    sensor_types = set()
    for document in instancesdb.find():
        sensor_types.add(document['sensor_type'])
    sensor_types = list(sensor_types)
    return sensor_types


def get_sensor_instances():
    sensor_instances = []
    for document in instancesdb.find():
        instance = {"sensor_type": document['sensor_type'], "id": document['_id']}
        sensor_instances.append(instance)
    return sensor_instances

def get_sensor_details(location):
    sensor_details = []
    for document in instancesdb.find():
        if document['geo_location'] == location:
            sensor_name = document['sensor_type'] + '_' + str(document['_id'])
            sensor_details.append(sensor_name)
    print(sensor_details)

# drop_db()
# register_sensors_from_json('sensor_config.json')