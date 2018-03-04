import math as m
import random as r
from heapq import*
import itertools
class priorityQueue():
    REMOVED = '<removed-task>'  # placeholder for a removed task
    def __init__(self):
        self.pq = []                         # list of entries arranged in a heap
        self.entry_finder = {}               # mapping of tasks to entries
        self.counter = itertools.count()     # unique sequence count
    def size(self):
        return len(self.pq)
    def empty(self):
        return len(self.pq)<1
    def add_task(self,task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove_task(task)
        self.count = next(self.counter)
        self.entry = [priority, self.count, task]
        self.entry_finder[task] = self.entry
        heappush(self.pq, self.entry)

    def remove_task(self,task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        self.entry = self.entry_finder.pop(task)
        self.pq.remove(self.entry)
        heapify(self.pq)

    def pop_task(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            self.priority, self.count, self.task = heappop(self.pq)
            #print(self.task)
            if self.task is not self.REMOVED:
                del self.entry_finder[self.task]
                return self.task
        raise KeyError('pop from an empty priority queue')

#returns a dict with each verticies edges. Links should be a list of tuples
def fromLinks(links):
    graph={}
    for link in links:
        for node in link:
            if not node in graph:
                graph[node]=[]
        graph[link[0]].append(link[1])
        graph[link[1]].append(link[0])
    return graph

#returns boolean value of whether or not graph contains eulerian trail
def eulerTrail(graph):
    countodds=[]
    for node in graph.keys():
        if not degree(graph, node)%2==0:
            countodds.append(node)
    if len(countodds)>2 or len(countodds)==1:
        return False
    if not isConnected(graph):
        return False
    else:
        return True
#returns boolean value of whether or not graph contains eulerian cycle
def eulerCycle(graph):
    if not isConnected(graph):
        return False
    for node in graph.keys():
        if not degree(graph,node)%2==0:
            return False
    return True
def pgraph(graph, edges):
    for vert in iter(graph):
        for toNodes in set(graph[vert]):
            print('From',vert,'to',toNodes,'is', length(vert,toNodes,edges))
#Returns number of edges to other verticies
def degree(graph, node):
    return(len(graph[node]))

#returns boolean indicating whether or not the graph contains a single component starting from vert
def isConnected(graph, vert=None):
    if vert==None:
        vert=list(graph.keys())[0]
    component=getComponent(graph, vert)
    allverts=set(graph.keys())
    for vert in allverts:
        if not vert in component:
            return False
    return True
##returns the component starting at node.
def getComponent(graph, node):
    visited=[]
    stack=[]
    stack.append(node)
    while not len(stack)<1:
        node=stack.pop()
        if not node in visited:
            visited.append(node)
            for toNode in graph[node]:
                stack.append(toNode)
    return visited
def Dijkstra(graph, source, edges=None):
    #comp=getComponent(graph,source)
    #for g in list(graph.keys()):
    #    if g not in comp:
    #        graph.pop(g,'ERROR')
    Q=priorityQueue()
    dist, prev={},{}
    dist[source]=0
    for vert in graph.keys():
        if not vert==source:
            dist[vert]=float('inf')
            prev[vert]=[]
        Q.add_task(vert, dist[vert])
    while not Q.empty():
        u=Q.pop_task()
        for v in graph[u]:
            alt=dist[u]+length(u,v,edges)
            if alt<dist[v]:
                dist[v]=alt
                prev[v]=u
                Q.add_task(v, alt)
    return dist, prev

def length(u, v, edges=None):
    if edges==None:
        return 1
    if (u,v) not in edges:
        return float('inf')
    connections=edges[(u,v)]
    connections=sorted(connections)
    return connections[0]

def testA():
    gruph=fromLinks([(1,2,),(1,4),(2,3,),(3,4),(5,6)])

    gaph={'A':['E','F','G','B'], 'B':['A','C'], 'C':['B','D']}
    gaph['D']=['C','G']
    gaph['G']=['A','D','F']
    gaph['F']=['E','A','G']
    gaph['E']=['A','F']
    print(eulerTrail(gruph))
    print(eulerTrail(gaph))
    print(eulerCycle(gaph))
    print(gruph)
    distances, route= Dijkstra(gaph, 'C')
    for node in distances.keys():
        print('Distance to '+ str(node)+ ":", distances[node])
        #print('Route to: ', route[node])
def testB():
    vertnames='ABCDEFGH'
    edges={}
    for ver in vertnames:
        if r.randint(1,4)>2:
            for i in range(r.randint(0,len(vertnames)//2)):
                if not str(vertnames[i])==str(ver):
                    templen= r.randint(1,20)
                    if(ver,vertnames[i]) in edges:
                        edges[(ver,vertnames[i])].append(templen)
                        edges[(vertnames[i],ver)].append(templen)
                    else:
                        edges[(ver,vertnames[i])]=[templen]
                        edges[(vertnames[i],ver)]=[templen]
    graph=fromLinks(list(edges.keys()))
    for v in vertnames:
        if v not in graph:
            graph[v]=[]
    #print(edges)
#    print(graph)
    print('RandoGraph is connected?', isConnected(graph,'A'))
    pgraph(graph,edges)
    dist, prev = Dijkstra(graph,'A', edges)
    printDij(dist,prev)
def printDij(dist, prev):
    for node in dist.keys():
        print('Shortest Distance to '+ str(node)+ ":", dist[node])
    print(prev)
def testC():
    graph={'B': [('A', 11), ('A', 5), ('C', 10), ('C', 19), ('D', 19)],
        'A': [('B', 11), ('B', 5), ('C', 11), ('D', 14)], 'C': [('B', 10),
        ('A', 11), ('B', 19), ('D', 2)], 'D': [('A', 14), ('B', 19), ('C', 2)]}
    print(length('B','A',graph))
    print(isConnected(graph,'D'))
#testC()
#testA()
testB()
