import sys
import datetime
from json import dumps


class Combinatorix(object):
    def __init__(self, source, destination, departure, arrival, flight_number):
        self.source = source
        self.destination = destination
        self.departure = datetime.datetime.strptime(departure, '%Y-%m-%dT%H:%M:%S')
        self.arrival = datetime.datetime.strptime(arrival, '%Y-%m-%dT%H:%M:%S')
        self.flight_number = flight_number.strip()

    def __str__(self):
        return '%s %s %s %s %s' % (self.source, self.destination, self.departure, self.arrival, self.flight_number)


def combine(item, object_array, container=None):
    if container is None:
        container = []
    for compare in object_array:
        delta = compare.departure - item.arrival
        latest = datetime.timedelta(hours=4)
        earliest = datetime.timedelta(hours=1)
        if earliest < delta < latest and item.destination == compare.source and item.source != compare.destination:
            entry = [{'A': item.flight_number + '' + item.destination,
                      'B': compare.flight_number + '' + compare.destination}]
            container.append(entry)
            combine(compare, object_array, entry)

    return container


def main():
    final_array = {'Flight_List': []}
    object_array = []
    data = sys.stdin.readlines()
    data.pop(0)  # remove first line
    for item in data:
        ary = item.split(',')
        x = Combinatorix(ary[0], ary[1], ary[2], ary[3], ary[4])
        object_array.append(x)

    for item in object_array:
        result = combine(item, object_array)
        if result:
            final_array['Flight_List'] += result

    sys.stdout.write(dumps(final_array))


main()
