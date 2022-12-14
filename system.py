from __future__ import annotations


class Station:

    def __init__(self, name, line):
        self.name = name
        self.line = line
        self.adjacent: list[Station] = []
        self.transfer: list[str] = None


class Line:

    def __init__(self, name, *station_infos):
        self.name = name
        self.station_names = []
        self.stations: list[Station] = []
        self._get_stations(*station_infos)
        
    def __contains__(self, station_name):
        return station_name in self.station_names
        
    def __iter__(self):
        return iter(self.stations)
    
    def get_station(self, station_name) -> Station:
        for station in self:
            if station.name == station_name:
                return station

    def _get_stations(self, *station_infos):
        paths = {}
        previous = None
        for station_info in station_infos:
            name, path = station_info.split('|')
            if name in self:
                station = self.get_station(name)
            else:
                self.station_names.append(name)
                station = Station(name, self.name)
                self.stations.append(station)
            if (key := path[:-1]) not in paths:
                paths[key] = previous
            elif key != list(paths.keys())[-1]:
                previous = list(paths.values())[-1]
                paths.popitem()
            if previous:
                previous.adjacent.append(station)
                if path[-1] == 't':
                    station.adjacent.append(previous)
            previous = station
               

class Subway:

    def __init__(self, name, *lines: Line):
        self.name = name
        self.lines = {line.name: line for line in lines}
        self._set_transfer()

    def _set_transfer(self):
        lines = list(self.lines.values())
        for i, line in enumerate(lines[:-1]):
            for station in line:
                if not station.transfer:
                    stations, transfers = [station], [line.name]
                    for another_line in (copy := list(lines).copy())[:i] + copy[i+1:]:
                        if another_station := another_line.get_station(station.name):
                            stations.append(another_station)
                            transfers.append(another_line.name)
                    if len(stations) > 1:
                        for station in stations:
                            station.transfer = [transfer for transfer in transfers if station.line != transfer]    