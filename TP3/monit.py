import psutil


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    # cpu_heat = psutil.sensors_temperatures()['coretemp'][0].current
    # print(f"CPU Usage: {usage}% and CPU Heat: {cpu_heat}°C")
    print(f"CPU Usage: {usage}%")


def check_ram_usage():
    usage = psutil.virtual_memory().percent
    print(f"RAM Usage: {usage}%")


#marche po
def check_ports_open(port):
    print(psutil.net_connections())
    if port in psutil.net_connections():
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")


if __name__ == "__main__":
    check_cpu_usage()
    check_ram_usage()
    check_ports_open(443)
