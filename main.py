import matplotlib.pyplot as plt
import subprocess
from datetime import datetime
import sys
from tqdm import tqdm


def app():

    def ping(host, size):
        response = subprocess.Popen(
            ["/bin/ping", "-c 1", f"-s {size}", host], stdout=subprocess.PIPE).stdout.read()
        time_eq = response.decode('utf-8').split(' ')[12][5:]
        return float(time_eq)


    def pinging(tries, size):
        with tqdm(mylist) as t:
            for i in range(tries):
                t.update()
                x_time.append(datetime.now())
                server_value.append(ping(ip_dict['server'], size))
                scaner_value.append(ping(ip_dict['scaner'], size))
                glbuh_valu.append(ping(ip_dict['glbuh'], size))
                router_value.append(ping(ip_dict['router'], size))

    if '-t' in sys.argv:
        tries = int(sys.argv[sys.argv.index('-t') + 1])
    else:
        tries = 100

    if '-s' in sys.argv:
        size = sys.argv[sys.argv.index('-s') + 1]
    else:
        size = 64

    mylist = [x for x in range(tries)]

    ip_dict = {
        'server': '192.168.1.2',
        'scaner': '192.168.1.36',
        'glbuh': '192.168.1.30',
        'router': '192.168.1.1'
    }

    x_time = []
    server_value = []
    scaner_value = []
    glbuh_valu = []
    router_value = []

    pinging(tries, size)

    plt.figure(figsize=(50, 5))
    plt.plot(x_time, server_value, label='server', marker='o')
    plt.plot(x_time, scaner_value, label='scaner', marker='o')
    plt.plot(x_time, glbuh_valu, label='glbuh', marker='o')
    plt.plot(x_time, router_value, label='router', marker='o')
    plt.ylabel('response time')
    plt.xlabel('time')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    app()
