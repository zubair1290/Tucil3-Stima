import os

class AdjGraf:
    def __init__(self, node):
        self.node = node
        self.matrix = [[0 for i in range(node)] for i in range(node)]
        self.name = ["" for i in range(node)]
    def add_edge(self, sc, dest, weight):
        self.matrix[sc][dest] = weight
    def add_all_edge(self, sc, neighbor):
        self.matrix[sc] = neighbor
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
    sum_node = len(lines[0].split())
    adj = AdjGraf(sum_node)
    for brs in range(sum_node):
        adj.add_all_edge(brs, lines[brs][:-1].split())

    for i, line in enumerate(lines[sum_node+1:sum_node*2+1]):
        adj.set_name(i, line[:-1])

print(adj.matrix, adj.name)

simpulhidup, bobot = "", 0
list_nhidup = [""]
print(list_nhidup)

list_w_ntog_nhidup = [["", ""]]
print(list_w_ntog_nhidup)

list_sum_w_ntog_nhidup = [0]
print(list_sum_w_ntog_nhidup)
goal = 4
curr_node = 0

# initialize
list_nhidup[0] = [str(curr_node)]
list_w_ntog_nhidup[0] = [0, 200]
list_sum_w_ntog_nhidup[0] = 200

print(list_nhidup)
print(list_w_ntog_nhidup)
print(list_sum_w_ntog_nhidup)

while True:
    # mencari simpul hidup yang nilai fungsi nya terkecil
    curr_idx = list_sum_w_ntog_nhidup.index(min(list_sum_w_ntog_nhidup))
    # simpul hidup
    simpulhidup = list_nhidup[curr_idx]
    # mencari node sekarang yang akan dibangkitkan
    curr_node = simpulhidup[-1]
    # mencari tetangganya
    neighbor = adj.neighbor(int(curr_node))
    print(neighbor)
    # iterasi
    for i in range(len(neighbor)):
        if neighbor[i] != '0':
            list_nhidup.append(simpulhidup + [str(neighbor[i])])
            list_w_ntog_nhidup.append([4, 200])            
            list_sum_w_ntog_nhidup.append(204)
    # delete 
    list_nhidup = list_nhidup[:curr_idx] + list_nhidup[curr_idx+1:]
    list_w_ntog_nhidup = list_w_ntog_nhidup[:curr_idx] + list_w_ntog_nhidup[curr_idx+1:]
    list_sum_w_ntog_nhidup = list_sum_w_ntog_nhidup[:curr_idx] + list_sum_w_ntog_nhidup[curr_idx+1:]
    print(curr_node)
    break

print(list_nhidup)
print(list_w_ntog_nhidup)
print(list_sum_w_ntog_nhidup)

