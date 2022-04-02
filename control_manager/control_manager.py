import control_db
import json
import control_server
import requests

def perform_action(sensor_type, sensor_location):
    ip, port = control_db.get_ip_and_port(sensor_type, sensor_location)
    response = requests.get('http://localhost:'+str(port)+'/performAction')
    print(response)

def registerControlInstance(instance):
    control_db.register_control_instance(instance)


def register_controllers_from_json(path):
    f = open(path)
    controllers = json.load(f)
    for instance in controllers['control_instances']:
        registerControlInstance(instance)


# def start_controllers():
#     control_instances = control_db.get_all_control_instances()
#     for controller in control_instances:
#         print(controller['sensor_type'])
#         control_server.start_server(controller['sensor_type'],
#                                     controller['sensor_ip'], controller['sensor_port'])
        
            