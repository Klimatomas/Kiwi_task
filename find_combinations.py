import sys
import datetime
from json import dumps


class Flight(object):
    def __init__(self, source, destination, departure, arrival, flight_number):
        self.source = source
        self.destination = destination
        try:
            self.departure = datetime.datetime.strptime(departure, '%Y-%m-%dT%H:%M:%S')
            self.arrival = datetime.datetime.strptime(arrival, '%Y-%m-%dT%H:%M:%S')
        except ValueError:
            sys.stderr.write("Wrong date format")
            quit()
        self.flight_number = flight_number.strip()


def __str__(self):
    return '%s %s %s %s %s' % (self.source, self.destination, self.departure, self.arrival, self.flight_number)


def combine(item, object_array, container):
    for compare in object_array:
        delta = compare.departure - item.arrival
        latest = datetime.timedelta(hours=4)
        earliest = datetime.timedelta(hours=1)
        if earliest < delta < latest and item.destination == compare.source and item.source != compare.destination:
            entry = [{'A': '%s %s' % (item.flight_number, item.destination),
                      'B': '%s %s' % (compare.flight_number, compare.destination)}]
            container.append(entry)
            combine(compare, object_array, entry)

    return container


def main():
    final_array = {'Flight_List': []}
    object_array = []
    data = sys.stdin.readlines()
    data.pop(0)  # remove first line
    for line in data:
        split_line = line.split(',')
        if len(split_line) != 5:
            sys.stderr.write("Wrong input")
            quit()
        x = Flight(split_line[0], split_line[1], split_line[2], split_line[3], split_line[4])
        object_array.append(x)

    for line in object_array:
        result = combine(line, object_array, [])
        if result:
            final_array['Flight_List'] += result

    sys.stdout.write(dumps(final_array))


main()
