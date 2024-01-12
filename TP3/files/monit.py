import psutil
import socket
from contextlib import closing
import json
import os


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    print(f"CPU Usage: {usage}%")
    return usage


def check_ram_usage():
    usage = psutil.virtual_memory().percent
    print(f"RAM Usage: {usage}%")
    return usage


def check_ports_open(host, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        if sock.connect_ex((host, port)) == 0:
            return True
        else:
            return False


def check_disk_usage():
    usage = psutil.disk_usage("/")[3]
    print(f"Disk Usage: {usage}%")
    return usage


def create_rapport(cpu_usage, ram_usage, disk_usage, ports_open):
    data = {"id":1,"data":{"cpu":cpu_usage,"ram":ram_usage,"disk":disk_usage,"ports":ports_open}}
    json_data = json.dumps(data)
    with open("rapport.json", "w") as f:
        f.write(json_data)


if __name__ == "__main__":
    with open("conf.json", "r") as f:
        config = json.load(f)
    host_ip = config["host"]
    ports = config["ports"]
    cpu=check_cpu_usage()
    ram=check_ram_usage()
    port_for_json={}
    for p in ports:
        if check_ports_open(host_ip, p):
            print(f"Port {p} is open")
            port_for_json[p]=True
        else:
            print(f"Port {p} is closed")
            port_for_json[p]=False
    disk=check_disk_usage()
    create_rapport(cpu, ram, disk, port_for_json)
