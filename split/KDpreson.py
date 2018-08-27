import sys
from math import sqrt
from collections import namedtuple
import json
from argparse import ArgumentParser

# do argument parser
parser = ArgumentParser()
parser.add_argument("file", help="Input your data file")
args = parser.parse_args()

class KdNode(object):
    def __init__(self, dom_elt, split, left, right):
        self.dom_elt = dom_elt 
        self.split = split   
        self.left = left    
        self.right = right    

class KdTree(object):
    def __init__(self, data):
        k = len(data[0]) 
        def CreateNode(split, data_set): 
            if not data_set: 
                return None
            data_set.sort(key=lambda x: x[split])
            split_pos = len(data_set) // 2  
            median = data_set[split_pos]        
            split_next = (split + 1) % k        
            return KdNode(median, split,CreateNode(split_next, data_set[:split_pos]),CreateNode(split_next, data_set[split_pos + 1:]))               
        self.root = CreateNode(0, data) 

# ====== KD search ======
result = namedtuple("Result_tuple", ['nearest_point', 'nearest_dist', 'nodes_visited']) 
def find_nearest(tree, point):
    k = len(point) 

    def travel(kd_node, target, max_dist):
        if kd_node is None:   
            return result([0] * k, float("inf"), 0)
        nodes_visited = 1    
        s = kd_node.split
        pivot = kd_node.dom_elt
        if target[s] <= pivot[s]:
            nearer_node = kd_node.left
            further_node = kd_node.right
        else:
            nearer_node = kd_node.right 
            further_node = kd_node.left 

        temp1 = travel(nearer_node, target, max_dist) 
        nearest = temp1.nearest_point
        # print(nearest)
        dist = temp1.nearest_dist
        # print(dist)
        nodes_visited  = temp1.nodes_visited 
        if dist < max_dist:   
            max_dist = dist  # 最近點將在以目標點為球心，max_dist為半徑的超球體內
            temp_dist = abs(pivot[s] - target[s])  
            if max_dist < temp_dist:        # 判斷超球體是否與超平面相交
                return result(nearest, dist, nodes_visited)
#---------------------------------------------------------------------- 
        temp_dist = sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(pivot, target)))   
        if temp_dist < dist:     # 如果“更近”
            nearest = pivot     
            dist = temp_dist    
            max_dist = dist 

        # another side
        temp2 = travel(further_node, target, max_dist)  
        nodes_visited  = temp2.nodes_visited
        if temp2.nearest_dist < dist: 
            nearest = temp2.nearest_point 
            dist = temp2.nearest_dist    
            return result(nearest, dist, nodes_visited)
        return result(nearest, dist, nodes_visited)

    # begin to travel from root
    return travel(tree.root, point, float("inf")) 

if __name__ == "__main__":
    data = []
    table = {}
    with open("districtTW.csv") as csv:
        for line in csv:
            lineSplit = line.split(',')
            loc = "["+lineSplit[1]+","+lineSplit[2]+"]"
            table[loc] = lineSplit[3]
            data.append([float(lineSplit[1]), float(lineSplit[2])])
    # data = [[2,3],[5,4],[9,6],[4,7],[8,1],[7,2]]
    kd = KdTree(data)
    person = {}
    with open(args.file) as csv:
        for line in csv:
            lineSplit = line.split()
            location = "["+lineSplit[3]+","+lineSplit[4]+"]"
            if person.get(lineSplit[0]) == None:
                ret = find_nearest(kd, [float(lineSplit[3]), float(lineSplit[4])])
                person[lineSplit[0]] = int(table["["+str(ret.nearest_point[0])+","+str(ret.nearest_point[1])+"]"])
    # ret = find_nearest(kd, [24.44864058, 121.6560593])
    # print(table["["+str(ret.nearest_point[0])+","+str(ret.nearest_point[1])+"]"])
    # print(person)
    
    # output json format for Table
    with open('T'+args.file, 'w') as fp:
        for key, value in person.items():
            print(key+" "+str(value), end="\n", file=fp)