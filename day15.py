initial = "9,19,1,6,0,5,4".split(',')

"""First star
while len(initial) <= 2020:
    last = initial[-1]
    if last in initial[:-1]:
        initial.reverse() # 0 4 5 0 6 1 19 9
        indexTruc = initial.index(last, 1)
        print(str(last) + " last seen reverse " + str(indexTruc))
        initial.reverse()
        indexTruc = len(initial) - (indexTruc + 1)
        print(str(last) + " last seen " + str(indexTruc))
        initial.append(str(len(initial) - indexTruc -1))
    else:
        initial.append('0')

print(initial)
print(last)"""

import networkx as nx
import matplotlib.pyplot as plt
initial = list(map(int, initial))
G = nx.Graph()

last = initial[0]
for node in initial[1:]:
    G.add_edge(node, last)
    last = node

nx.draw(G, with_labels=True)
plt.show()

while G.number_of_edges() < 30000000:

    if last in G.all_successors(last):
        dif = nx.shortest_path_length(G, last, last)
        print(dif)
    else:
        G.add_edge(0, last)
        last = 0


nx.draw(G, with_labels=True)
plt.show()
