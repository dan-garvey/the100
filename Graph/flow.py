import collections
 
# This class represents a directed graph using adjacency matrix representation
class Graph:
  
    def __init__(self,graph):
        self.graph = graph # residual graph
        self.ROW = len(graph)
  
    def BFS(self,s, t, parent):
        '''Returns true if there is a path from source 's' to sink 't' in
        residual graph. Also fills parent[] to store the path '''
        ans = False
        # Mark all the vertices as not visited
        visited = [False] * (self.ROW)
         
        # Create a queue for BFS
        queue = collections.deque()
         
        # Mark the source node as visited and enqueue it
        for source in s:
          queue.append(source)
          visited[source] = True
         
        # Standard BFS Loop
        while queue:
            u = queue.popleft()
         
            # Get all adjacent vertices's of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0 :
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
 
        # If we reached sink in BFS starting from source, then return
        # true, else false
        for sink in t:
          ans = ans or visited[sink]
        return ans
             
    # Returns the maximum flow from s to t in the given graph
    def EdmondsKarp(self, source, sink):
 
        # This array is filled by BFS and to store path
        parent = [-1] * (self.ROW)
 
        max_flow = 0 # There is no flow initially
 
        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent) :
 
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink[0]
            while s not in source:
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
 
            # Add path flow to overall flow
            max_flow +=  path_flow
 
            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while v !=  source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
 
        return max_flow
def answer(entrances, exits, path):
  graph = Graph(path)
  return graph.EdmondsKarp(entrances, exits)
  
"""def supers(entrances, exits, path):
  newPath = len(path)-len(exits)-len(entrances)
  newPath = [newPath*[0]]*newPath
  supersource = [0]*len(path)
  supersink= [0]*len(path)
  graph = Counter()
  for i in entrances:
    for j in node
    graph['s']+=
  for layer in entrances:
    #print(supersource)
    supersource = map(add, supersource, path[layer])
  for layer in exits:
    supersink = map(add, supersink, path[layer])
  
    
  path = path[len(entrances):]
  return supersource, supersink, path
"""
entrances = [0, 1]
exits = [4, 5]
path = [
  [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
  [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
  [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
  [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
  [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
  [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
]

#source, sink, path = supers(entrances, exits, path)
print answer(entrances, exits, path)
"""
test1 = (entrances, exits, path)
entrances2 = [0]
exits2 = [3]
path2 = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]
out2= 6
test2 =(entrances, exits, path)

out1 = 16"""
