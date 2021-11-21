from collections import deque
class Graph:
    def __init__(self,n):
        self.vertices = [-1] * n
        self.links = [None] * n 
        self.visited = [False] * n
    
    def connect(self,x,y):
        if self.links[x]:
            self.links[x].append(y)
        else: 
            self.links[x] = [y]
        if self.links[y]:
            self.links[y].append(x)
        else:
            self.links[y] = [x]

    def find_all_distances(self,s):
        self.visited[s] = True 
        BFSQ = deque()
        if not self.links[s]:
            self.links[s]=[]
        for vertex in self.links[s]:
            BFSQ.append([vertex,0])
        
        while BFSQ:
            nodeDistance = BFSQ.popleft()
            node,distance = nodeDistance[0],nodeDistance[1]
            if self.visited[node]:
                continue
            self.visited[node] = True
            shortestDistance = distance + 6
            self.vertices[node]= shortestDistance
            for subNode in self.links[node]:
                BFSQ.append([subNode,shortestDistance])

        del self.vertices[s]
        print(" ".join([str(x) for x in self.vertices]))
