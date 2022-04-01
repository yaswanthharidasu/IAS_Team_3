import mongo
import kafka_manager
import threading

def registerSensorType(sensor_type):
    mongo.register_sensor_type(sensor_type)


def registerSensorInstance(sensor_instance):
    mongo.register_sensor_instance(sensor_instance)


def getSensorData(topic_name):
    # Start producing data for the newly added sensor
    kafka_manager.create_kafka_topic(topic_name)
    threading.Thread(target=kafka_manager.produce_data, args=(topic_name,)).start()

    # TODO: send data


def getSensorTypes():
    return mongo.get_sensor_types()


def getSensorDetails(location):
    return mongo.get_sensor_details(location)

getSensorData("light_4")