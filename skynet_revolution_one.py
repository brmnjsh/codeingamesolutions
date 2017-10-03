import sys
import math

# Skynet Revolution - Episode 1
# https://www.codingame.com/ide/puzzle/skynet-revolution-episode-1

def graphLinks(linkOrigin,links,linkPath):
    choice = None;
    for l in links: #iterate through links
        if linkOrigin in l:
            choice = l
            found = False;
            for p in l:
                if p in graph["gateways"]:
                    print("found", p, file=sys.stderr)
                    found = True
                    break
            if found == True: break
                
    print(choice[0],choice[1])
                

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
graph = {"nodes":[], "gateways":[], "links":[]}
linkPaths = []

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]

for i in range(n):
    graph["nodes"].append({"links": [], "gateway": 0})

for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    graph["nodes"][n1]["links"].append([n1, n2])
    graph["links"].append([n1,n2])
    
for i in range(e):
    ei = int(input())  # the index of a gateway node
    graph["nodes"][ei]["gateway"] = 1
    graph["gateways"].append(ei)
    
print(graph, file=sys.stderr)
    
# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    # To debug: print("Debug messages...", file=sys.stderr)
    #print(si, graph["gateways"], graph["links"], file=sys.stderr)   
    graphLinks(si,graph["links"],[])