import os
import geopy

geolocator = geopy.geocoders.Nominatim(user_agent="geoapiExercises")

class AdjGraf:
    def __init__(self, node: int):
        self.node = node
        self.matrix = [[0 for i in range(node)] for i in range(node)]
        self.location = ["" for i in range(node)]
    def add_edge(self, sc: int, dest: int, weight):
        self.matrix[sc][dest] = weight
    def add_all_edge(self, sc: int, neighbor: list):
        self.matrix[sc] = neighbor
    def neighbor(self, node: int):
        return self.matrix[node]
    def set_location(self, node: int, location):
        self.location[node] = location
    
def haversine(location1: tuple, location2: tuple) -> float:
    from math import sin, cos, pow, sqrt, asin, pi
    latitude1, longitude1 = tuple(map(lambda x: (x*pi) / 180.0, location1))
    latitude2, longitude2 = tuple(map(lambda x: (x*pi) / 180.0, location2))
    dif_lat = latitude2 - latitude1
    dif_long = longitude2 - longitude1
    earth_radius = 6_371_230 # meters
    return 2*earth_radius*asin(sqrt(pow(sin(dif_lat/2), 2) + cos(latitude1)*cos(latitude2)*pow(sin(dif_long/2), 2)))


DIRECTORY = "../test/"
# files = os.listdir(DIRECTORY)
# for file in files:
#     pass
# matrixEdge = []

# file
file = input()

# matrix graf
adj = None

# src to dest
src, dest = None, None


with open(DIRECTORY + file, "r") as rf:
    lines = rf.readlines()
    sum_node = len(lines[0].split())
    adj = AdjGraf(sum_node)
    src = int(lines[-2][:-1])
    dest = int(lines[-1][:-1])
    for brs in range(sum_node):
        adj.add_all_edge(brs,  list(map(int, lines[brs][:-1].split())))

    for i, line in enumerate(lines[sum_node+1:sum_node*2+1]):
        adj.set_location(i, tuple(map(float, line[:-1].split(", "))))
    del brs, sum_node, i, line, lines, DIRECTORY, file

print(adj.matrix, adj.location)

simpulhidup, bobot = [0], 0
list_nhidup = [[0]]
print(list_nhidup)

list_w_ntog_nhidup = [[0, 200]]
print(list_w_ntog_nhidup)

list_sum_w_ntog_nhidup = [0]
print(list_sum_w_ntog_nhidup)
curr_node = src

# initialize
list_nhidup[0] = [curr_node]
heuristic_ntog = haversine(adj.location[curr_node], adj.location[dest])
list_w_ntog_nhidup[0] = [0, heuristic_ntog]
list_sum_w_ntog_nhidup[0] = heuristic_ntog

print(list_nhidup)
print(list_w_ntog_nhidup)
print(list_sum_w_ntog_nhidup)
while True:
    # mencari simpul hidup yang nilai fungsi nya terkecil
    curr_idx = list_sum_w_ntog_nhidup.index(min(list_sum_w_ntog_nhidup))
    # simpul hidup
    simpulhidup = list_nhidup[curr_idx]
    # mencari node sekarang yang akan dibangkitkan
    curr_node = int(simpulhidup[-1])
    print(curr_node)
    # jika node sekarang adalah node tujuan maka pencarian berhenti
    if curr_node == dest: break
    # mendelete penelusuran simpul hidup node, bobot nya dan heuristicnya
    list_nhidup = list_nhidup[:curr_idx] + list_nhidup[curr_idx+1:]
    list_w_ntog_nhidup = list_w_ntog_nhidup[:curr_idx] + list_w_ntog_nhidup[curr_idx+1:]
    list_sum_w_ntog_nhidup = list_sum_w_ntog_nhidup[:curr_idx] + list_sum_w_ntog_nhidup[curr_idx+1:]
    # mencari tetangganya
    neighbor = adj.neighbor(curr_node)

    # iterasi
    for node in range(len(neighbor)):
        old_simpulhidup = simpulhidup.copy()
        if neighbor[node] != 0 and node not in simpulhidup:
            # push
            simpulhidup.append(node)
            list_nhidup.append(simpulhidup)
            # haversine()
            weight = haversine(adj.location[curr_node], adj.location[node])
            heuristic_ntog = haversine(adj.location[node], adj.location[dest])
            list_w_ntog_nhidup.append([weight, heuristic_ntog])
            list_sum_w_ntog_nhidup.append(weight+heuristic_ntog)
        simpulhidup = old_simpulhidup
        del old_simpulhidup
    print(list_nhidup)

print(simpulhidup)