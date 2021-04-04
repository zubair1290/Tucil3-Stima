import os
import numpy as np

class AdjGraf:
    def __init__(self, node):
        self.node = node
        self.matrix = np.zeros((node, node), dtype='i')
        self.name = ["" for i in range(node)]
        self.name = np.zeros(node, dtype='O')
    def add_edge(self, sc, dest, weight):
        self.matrix[sc][dest] = weight
    def neighbor(self, node):
        return self.matrix[node]
    def set_name(self, node, name):
        self.name[node] = name

DIRECTORY = "../test/"
# files = os.listdir(DIRECTORY)
# for file in files:
#     pass
# matrixEdge = []
file = input()
adj = None
with open(DIRECTORY + file) as rf:
    lines = rf.readlines()
    adj = AdjGraf(lines[0].count(' ')+1)
    brs = 0
    for line in lines:
        if line[0] == '-': break
        kol, weight = 0, ""
        for cc in line[:-1]:
            if cc == ' ':
                adj.add_edge(brs, kol, int(weight))
                kol += 1
                weight = ""
            else:
                weight += cc
        adj.add_edge(brs, kol, int(weight))
        brs += 1
    del weight, brs, kol
    # for cc in lines[-1]:
    #     if (cc == "\""):
    #         continue
    #     if cc == ' ':
    #         print(road)
    #         adj.set_name(kol, road)
    #         kol += 1
    #         road = "a"
    #     else:
    #         pass
    #         road += str(cc)
    #         print(road)
    kol = 0
    road = ""
    i = 1
    line = lines[-1]
    while i < line.__len__():
        if line[i] == '\"':
            adj.set_name(kol, road)
            print(road)
            kol += 1
            road = ""
            i += 2
        else:
            road += line[i]
        i+=1
    del road, line, lines, cc

    # adj.set_name(kol, road)

    # while (f_readc != '-'):
    #     if (f_readc == ' '):
    #         line.append(int(weight))
    #         weight = ""
    #         kol += 1
    #     elif (f_readc == '\n'):
    #         line.append(int(weight))
    #         matrixEdge.append(line)
    #         line, weight = [], ""
    #     else:
    #         weight += f_readc
    #     f_readc = rf.read(1)
    # rf.read(2)


    # f_readc = rf.read(1)
    # line, road = [], ""
    # while (f_readc):
    #     if (f_readc == "\""):
    #         line.append(road)
    #         road = ""
    #         rf.read(2)
    #     else:
    #         road += f_readc
    #     f_readc = rf.read(1)
    # roads = line
    # del road, line, weight, f_readc

del DIRECTORY, file
# # print(matrixEdge)
# adj = AdjGraf(len(matrixEdge))
# for i in range(len(matrixEdge)):
#     for j in range(i, len(matrixEdge)):
#         if matrixEdge[i][j] != 0:
#             adj.add_edge(i, j, matrixEdge[i][j])
# del matrixEdge
# for i in range(len(roads)):
#     adj.set_name(i, roads[i])
print(adj.matrix, adj.name)
# print(adj.name)
# del roads
simpulhidup, bobot = [], 0
list_simpulhidup, list_bobot_simpulhidup = [], []
curr_simpul = 0


