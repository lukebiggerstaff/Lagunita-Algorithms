import sys
import re
import math

def read_file(plot):
    data = []
    with open(plot) as f:
        for line in f:
            line_lst = [float(x) for x in line.rsplit()]
            data.append(line_lst)
    return data

def find_distance(plot1, plot2):
    x = plot1[0]
    y = plot1[1]
    z = plot2[0]
    w = plot2[1]
    # Euclidean distance formula
    distance = math.sqrt(
        (x - z) ** 2 + (y - w) ** 2
    )
    return distance




if __name__ == '__main__':
    data = read_file(sys.argv[1])
    distance = find_distance(data[0], data[1])
    print(distance)
