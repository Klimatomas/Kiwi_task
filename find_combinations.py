import sys
import datetime
from json import dumps


class Combinatorix(object):
    def __init__(self, source, destination, departure, arrival, flight_number):
        self.source = source
        self.destination = destination
        self.departure = datetime.datetime.strptime(departure, "%Y-%m-%dT%H:%M:%S")
        self.arrival = datetime.datetime.strptime(arrival, "%Y-%m-%dT%H:%M:%S")
        self.flight_number = flight_number.strip()

    def __str__(self):
        return "%s %s %s %s %s" % (self.source, self.destination, self.departure, self.arrival, self.flight_number)


def method(item, arr, na=None):
    if na is None:
        na = []
    for i in arr:
        delta = i.departure - item.arrival
        x = datetime.timedelta(hours=4)
        y = datetime.timedelta(hours=1)
        if y < delta < x and item.destination == i.source and item.source != i.destination:
            x = [{"A": item.flight_number + item.destination, "B": i.flight_number + i.destination}]
            na.append(x)
            method(i, arr, x)
        else:
            pass
    return na


def main():
    final_arr = []
    arr = []
    data = sys.stdin.readlines()
    data.pop(0)  # remove first line
    for item in data:
        ary = item.split(",")
        x = Combinatorix(ary[0], ary[1], ary[2], ary[3], ary[4])
        arr.append(x)

    for item in arr:
        result = method(item, arr)
        if result:
            final_arr.append(result)

    print dumps(final_arr)

main()
