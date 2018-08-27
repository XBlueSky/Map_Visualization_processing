import json
from argparse import ArgumentParser

# do argument parser
parser = ArgumentParser()
parser.add_argument("file", help="Input your data file")
parser.add_argument("-t", "--table", help="Allocate people to corresponding district by mapping table ", dest="table", default="T2018053100")
args = parser.parse_args()

# initial
mapTable = {}
result = {}

with open(args.table) as table:
    for line in table:
        lineSplit = line.split()
        if int(lineSplit[1]) <= 12:
            mapTable[lineSplit[0]] = lineSplit[1]
            if result.get(lineSplit[1]) == None:
                result[lineSplit[1]] = {}

with open(args.file) as csv:
    for line in csv:
        lineSplit = line.split()
        if mapTable.get(lineSplit[0]) != None:
            info = {
                'begin': lineSplit[1],
                'end': lineSplit[2],
                'lat': lineSplit[3],
                'lon': lineSplit[4]
            }
            # combine info data by ID
            distrctID = mapTable[lineSplit[0]]
            if result[distrctID].get(lineSplit[0]) == None:
                result[distrctID][lineSplit[0]] =  {}
                result[distrctID][lineSplit[0]]['date'] = args.file
                result[distrctID][lineSplit[0]]['info'] = []
            result[distrctID][lineSplit[0]]['info'].append(info)

# print(result)

# distrctCount = 1
# output json format
for itemKey, item in result.items():
    count = 1
    with open(itemKey+'d'+args.file+'.json', 'w') as fp:
        print("[", end="\n",file=fp)
        for key, value in item.items():
            print("{'name' : " + key, end=",\n", file=fp)
            print("'date' : " + value['date'], end=",\n", file=fp)
            strList = ','.join(map(str, value['info']))
            print("'info' : [" + strList, end="]}", file=fp)
            if count != len(item):
                print(",\n", end="", file=fp)
            count += 1 
        print("\n]", file=fp)
    