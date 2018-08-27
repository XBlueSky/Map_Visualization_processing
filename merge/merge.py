import json
from argparse import ArgumentParser

# do argument parser
parser = ArgumentParser()
parser.add_argument("file", help="Input your data file")
args = parser.parse_args()

# initial
content = []
compare = {
    'id': 0,
    'begin': 0,
    'end': 0,
    'lat': 0,
    'lon': 0
}

with open(args.file) as csv:
    for i, line in enumerate(csv):
        lineSplit = line.split()
        info = {
            'id': lineSplit[0],
            'begin': lineSplit[1],
            'end': lineSplit[2],
            'lat': lineSplit[3],
            'lon': lineSplit[4]
        }
        # merge the same person who has been in identical location for continous time to lighten file size.
        # if compare['id'] == info['id'] and compare['lat'] == info['lat'] and compare['lon'] == info['lon']:
        #     compare['end'] = info['end']
        # else:
        # if i != 0:
        content.append(info)
            # compare = info

filename = args.file.split('_')

with open(filename[1], 'w') as fp:
    for item in content:
        print >> fp, item['id'], item['begin'], item['end'], item['lat'], item['lon']