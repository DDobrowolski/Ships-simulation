import csv
from models.Port import Port
from models.Container import Container
import random

content_types = ['Drewno', 'Metal', 'Paliwo']


def load_from_csv():
    ports = []
    with open('const/ports.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            if row[0] == 'name':
                continue
            ports.append(
                Port((row[1], row[2]), row[0], 5, []))
    add_containers_to_ports(ports)
    return ports


def add_containers_to_ports(ports):
    for port in ports:
        port.containers_out = generate_containers_list(port, ports)


def generate_containers_list(source, ports):
    containers = []
    for i in range(1, 5000):
        new_container = Container(source, random.choice(
            ports), random.choice(content_types))
        containers.append(new_container)
    return containers
