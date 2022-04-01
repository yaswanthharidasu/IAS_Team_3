import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["SensorDatabase"]
instancesdb = mydb["SensorInstances"]
# types = mydb["SensorTypes"]

# Deprecated
# def register_sensor_type(sensor_type):
#     types = mydb["SensorTypes"]
#     types.insert_one(sensor_type)

def drop_db():
    instancesdb.drop()
    client.drop_database("SensorDatabase")

def getCount(obj):
    return obj.count_documents({})

def register_sensor_instance(sensor_instance):
    count = getCount(instancesdb)
    sensor_instance['_id'] = count+1
    instancesdb.insert_one(sensor_instance)

def get_sensor_types():
    for document in instancesdb.find():
        print(document) 

drop_db()