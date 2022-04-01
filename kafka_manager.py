from time import sleep
from kafka import KafkaProducer, KafkaConsumer
import json
import sensor_data
import threading
import mongo

bootstrap_servers = ['localhost:9092']

def get_sensor_instances():
    sensor_instances = get_sensor_instances()
    return sensor_instances


def create_kafka_topic(topic_name):
    '''Creates Kafka topic'''
    consumer = KafkaConsumer(topic_name,
                            bootstrap_servers=bootstrap_servers,
                            auto_offset_reset='earliest')
                            # value_deserializer=lambda m: json.loads(
                            #      m.decode('utf-8'))
    # for message in consumer:
    #     # print(message)
    #     print("brightness:", message[6]['brightness'])


def produce_data(topic_name):
    print("hello")
    '''Produces data and store into the topic'''
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    # value_serializer=lambda v: json.dumps(v).encode('utf-8')
    while(True):
        data = sensor_data.produceData(topic_name)
        producer.send(topic_name, bytes(str(data),'utf-8'))
        sleep(1)


def produce_sensors_data():
    sensor_instances = mongo.get_sensor_instances()
    for instance in sensor_instances:
        # Creating thread for each sensor instance
        topic_name = instance['sensor_type'] + '_' + str(instance['id'])
        print(topic_name)
        create_kafka_topic(topic_name)
        threading.Thread(target=produce_data, args=(topic_name,)).start()
    