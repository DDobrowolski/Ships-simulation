import csv
from models.Port import Port


def load_from_csv():
    ports = []
    with open('const/ports.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            if row[0] == 'name':
                continue
            ports.append(
                Port((row[1], row[2]), 5, None, None))
    return ports
