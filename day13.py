planning = """1000104
41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,659,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,937,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17"""
minimum, buses = planning.split("\n")
buses = buses.split(',')

"""First star
buses = list(filter(('x').__ne__, buses))
buses = list(map(int, buses))
best = None
time = int(minimum)
i = 0

while not best:
    for bus in buses:
        if(time % bus == 0):
            wait = time - int(minimum)
            best = bus
            break
    time += 1
print(best * wait)"""

earliest = None
offsets = {}
buses2 = []
for offset, bus in enumerate(buses):
    if bus == 'x':
        pass
    else:
        buses2.append(bus)
        offsets[bus] = offset
print(offsets)
print (buses2)

for time in range(99999999999963, 10000000000000000000, 41):
    earliest = time
    for bus in buses2:
        if (time + offsets[bus]) % int(bus) != 0:
            earliest = None
            break
    if earliest:
        break
print(earliest)