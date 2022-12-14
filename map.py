from system import *


lines = []
with open('stations.txt') as f:
    for line in f:
        name, station_names = line.split(':')
        lines.append(Line(name, *station_names.rstrip().split('-')))

subway = Subway('수도권 전철', *lines)
