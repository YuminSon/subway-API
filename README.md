# subway-API
API that helps build a subway object with interconnected stations and lines

## Key Points
- Can handle multiple paths, circulative parts, and one-way designs in subway lines.
- Automatically detects transfer stations.
- Comes with Seoul Metropolitan Subway for example.

## Usage
0. You need to have Python>=3.8 configured.
1. Copy the three files and save it on your system.
2. Import `subway` from `map.py` to get access to Seoul Metropolitan Subway object, or configure your own subway map.

## Details
- Each `Station` instance has `name`, `line`, `adjacent`, and `transfer` attributes. `adjacent` is a list with the `Station` instances of stations that are directly connected. `transfer` is a list that holds the names of the lines that also has a `Station` instance of the same name.
- `Line` instances have `name`, `station_names`, and `stations` attributes. While `stations` is a list of the `Station` instances the line has, `station_names` is consisted of the names of the stations.
- A `Subway` instance is defined with a name and the lines it covers. The attribute `lines` is a dictionary that has the line names as the keys and the `Line` instances as the values.
- In order to create your own subway system, first edit `stations.txt` and remove or add stations. The syntax is as follows in EBNF. 'o' stands for 'one-way', and 't' for 'two-way'.
```EBNF
syntax: line_name, ':', stn_info_list
line_name: ? line name ?
stn_info_list:
  | stn_info
  | stn_info, '-', stn_info_list
stn_info: stn_name, '|', path_name, one-way_indicator
stn_name: ? station name ?
path_name: ? user-defined path name ?
one-way_indicator: 'o' | 't'
```
- Then, edit `map.py` to instantiate the `Line` class from each line in `stations.txt`. Instances of class `Station` will be created accordingly with appropriate `adjacent` attributes.
- Finally, initialize a `Subway` instance with the lines you created. The `transfer` attributes will be filled in this stage. The instance is now ready for import and use.

## License
BSD 3-Clause
