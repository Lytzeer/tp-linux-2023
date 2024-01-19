import argparse
import psutil
import socket
from contextlib import closing
import json
import uuid
import time
import os
import logging

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
            print(f"Port {port} is open")
            return True
        else:
            print(f"Port {port} is closed")
            return False


def check_disk_usage():
    usage = psutil.disk_usage("/")[3]
    print(f"Disk Usage: {usage}%")
    return usage


def create_rapport(cpu_usage, ram_usage, disk_usage, ports_open):
    data = {"id":str(uuid.uuid4()),"time":time.strftime("%d/%m/%Y %H:%M:%S"),"data":{"cpu":cpu_usage,"ram":ram_usage,"disk":disk_usage,"ports":ports_open}}
    json_data = json.dumps(data)
    with open(f"var/monit/{data["id"]}.json", "w") as f:
        f.write(json_data)
        logging.info(f"Report created with id {data["id"]}")


def create_rapport_file(id:str):
    os.mkdir("var/monit/"+id)


def check(config):
    host_ip = config["host"]
    ports = config["ports"]
    cpu=check_cpu_usage()
    ram=check_ram_usage()
    port_for_json={}
    for p in ports:
        port_for_json[p]=check_ports_open(host_ip, p)
    disk=check_disk_usage()
    create_rapport(cpu, ram, disk, port_for_json)

def get_config():
    with open("etc/monit/conf.d/conf.json", "r") as f:
        config = json.load(f)
    return config

def get_last_rapport():
    last=None
    for file in os.listdir("var/monit"):
        if last is None:
            last = file
        elif os.path.getmtime(f"{"var/monit"}/{file}") > os.path.getmtime(f"{"var/monit"}/{last}"):
            last = file
    with open(f"{"var/monit"}/{last}", "r") as f:
        content = json.load(f)
        logging.info(f"Get last report:{content["id"]}")
        return content

def get_all_reports():
    rapport_list=[]
    for file in os.listdir("var/monit/"):
        with open(f"var/monit//{file}", "r") as f:
            rapport_list.append(json.load(f))
    logging.info(f"Get all reports")
    return rapport_list

def get_report(name):
    if os.path.exists(f"var/monit/{name}"):
        with open(f"var/monit/{name}", "r") as f:
            return json.load(f)
    else:
        print("File not found")
        return None

def get_rapports_younger_than(hours):
    rep=[]
    for file in os.listdir("var/monit/"):
        if time.time() - os.path.getmtime(f"var/monit/{file}") < hours*60*60:
            rep.append(file)
    return rep    

def get_avg_of_report(hours):
    rapports=get_rapports_younger_than(hours)
    rep=None
    for rapport in rapports:
        r=get_report(rapport)
        if rep is None:
            rep = r
        else:
            rep["data"]["cpu"] += r["data"]["cpu"]
            rep["data"]["ram"] += r["data"]["ram"]
    if rep is not None:
        rep["data"]["cpu"] /= len(rapports)
        rep["data"]["ram"] /= len(rapports)
        json_data = {"cpu":rep["data"]["cpu"],"ram":rep["data"]["ram"]}
        logging.info(f"Get avg of reports younger than {hours} hours")
        return json_data
    else:
        return None
    

def log_config():
    logging.basicConfig(filename='var/log/monit/monit.log', encoding='utf-8', level=logging.DEBUG)

def check_init():
    if not os.path.exists("var/monit"):
        print("var/monit not found \nPlease run init.sh")
    if not os.path.exists("var/log/monit"): 
        print("var/log/monit not found \nPlease run init.sh")
    if not os.path.exists("etc/monit/conf.d"):
        print("etc/monit/conf.d not found \nPlease run init.sh")
        return False
    else:
        return True
        

if __name__ == "__main__":
    if not check_init():
        exit()
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="Commande à executer", choices=["check", "list", "get"])
    parser.add_argument("parameter", help="Le paramètre de la commande", nargs='*', default='')
    args = parser.parse_args()
    log_config()

    match args.command:
        case "check":
            check(get_config())
        case "list":
            print(get_all_reports())
        case "get":
            match args.parameter[0]:
                case "last":
                    print(get_last_rapport())
                case "avg":
                    print(get_avg_of_report(int(args.parameter[1])))
                case _:
                    print(get_report(args.parameter[0]))
        case _:
            print("Commande inconnue")