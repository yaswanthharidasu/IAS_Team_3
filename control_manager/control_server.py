import threading
import fan_server
import ac_server

def start_server(sensor_type, ip, port):
    if sensor_type == 'fan':
        print("Starting fan server at:", ip, port)
        threading.Thread(target=lambda: fan_server.start_server(ip, port)).start()
    elif sensor_type == 'ac':
        print("Starting ac server at:", ip, port)
        threading.Thread(target=lambda: ac_server.start_server(ip, port)).start()
        # ac_server.start_server(ip, port)
