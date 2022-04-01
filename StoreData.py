import pymongo


def register_sensor():

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    database = myclient["SensorDatabase"]             #creating a database

    instance_coll = database["sensor_instances"]

    registration_coll = database["sensor_registration"]

    Sensor_Type =[
                    {
                        "sensor_type_id": "1",
                        "sensor_type_name": "temp",
                        "data": {
                            "temp": "float"
                        },
                    },
                    {
                        "sensor_type_id": "2",
                        "sensor_type_name": "moisture",
                        "data": {
                            "moisture": "float"
                        },  
                    }
        ]

    Sensor_instance = [
        {
            "1": [
                {
                    "sensor_id": 1,
                    "location" : "Vindhya",
                },
                {
                    "sensor_id":2,
                    "location":"GH",
                }
            ]
        },
        {
            "2":[
                
                {
                    "sensor_id": 1,
                    "location" : "OBH",
                }
            ]
            
        }
    ]

    

    
    for each_type in Sensor_Type:
        registration_coll.insert_one(each_type)
        # print(each_type)

    for each_instance in Sensor_instance:
        instance_coll.insert_one(each_instance)
        # print(each_instance)
    
   


def get_sensor_type():
    
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    database = myclient["SensorDatabase"]             #creating a instance database
    registration_coll = database["sensor_registration"]

    sensor_dict = dict()

    for i in registration_coll.find({},{ "_id": 0}):
            sensor_dict[i["sensor_type_id"]] = i["sensor_type_name"]
            # print(i)
            # print()
    return sensor_dict

def get_sensor_instance(n):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    database = myclient["SensorDatabase"]             #creating a instance database
    instance_coll = database["sensor_instances"]

    lis = []
    for i in instance_coll.find({},{ "_id": 0,n:1}):
        if i != {}:
            # print(i[n])
            for instances in i[n]:
                # print(instances["sensor_id"])
                lis.append(instances["sensor_id"])

    return lis


def get_sensor_instance2(n,loc):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    database = myclient["SensorDatabase"]             #creating a instance database
    instance_coll = database["sensor_instances"]

    lis = []
    for i in instance_coll.find({},{ "_id": 0,n:1}):
        if i != {}:
            # print(i[n])
            for instances in i[n]:
                # print(instances["sensor_id"])
                if(instances["location"] == loc):
                    lis.append(instances["sensor_id"])

    return lis

def delete_db():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    database = myclient["SensorDatabase"]             #creating a instance database
    registration_coll = database["sensor_registration"]
    instance_coll = database["sensor_instances"]

    registration_coll = database["sensor_registration"]


    # database.instance_coll.find().sort({"_id":-1}).limit(1).pretty()


    instance_coll.drop()
    registration_coll.drop()

    myclient.drop_database("InstanceDatabase")


if __name__ == "__main__":

    delete_db()
    register_sensor()
    sensor_dict = get_sensor_type()
    for sensor_type,sensor_name in sensor_dict.items():
        print(sensor_type,sensor_name)

    instance_lis = get_sensor_instance("1")

    print("Sensor instances we got in case 1")
    for each_ins in instance_lis:
        print(each_ins)

    print("Sensor instances we got in case 2")
    instance_lis2 = get_sensor_instance2("1","GH")
    for each_ins in instance_lis2:
        print(each_ins)


