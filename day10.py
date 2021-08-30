adapters = """133
157
39
74
108
136
92
55
86
46
111
58
80
115
84
67
98
30
40
61
71
114
17
9
123
142
49
158
107
139
104
132
155
96
91
15
11
23
54
6
63
126
3
10
116
87
68
72
109
62
134
103
1
16
101
117
35
120
151
102
85
145
135
79
2
147
33
41
93
52
48
64
81
29
20
110
129
43
148
36
53
26
42
156
154
77
88
73
27
34
12
146
78
47
28
97"""
adapters = list(map(int, adapters.split()))
adapters.sort()
"""first star
sum1 = 1
sum2 = 0
sum3 = 1


while(len(adapters) > 1):
    adapt = adapters.pop(adapters.index(min(adapters)))
    if min(adapters) - adapt == 1:
        sum1 += 1
    elif min(adapters) - adapt == 2:
        sum2 += 1
    elif min(adapters) - adapt == 3:
        sum3 += 1
    else:
        print("bruh")
print(sum1 * sum3)
"""
import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph()

adapters.append(0)
for node in adapters:
    G.add_node(node)

for node in adapters:
    for nod in adapters:
        if 0 < nod - node <= 3:
            G.add_edge(node, nod)
count = 0

#nx.draw_networkx(G, with_labels=True)
#plt.show()
print(G.number_of_edges())
print(G.number_of_nodes())

final_paths = list()
alternate_paths = set()

node = max(adapters)

def f(node):
    for pred in G.predecessors(node):
        if

print(len(final_paths))
nx.draw_networkx(G)
plt.show()