from collections import deque

class Node:
    def __init__(self,i):
        self.index = i
        self.destance = -1
        self.Adjesants = []
        self.visited = False

class Graph:
    def __init__(self,n):
        self.NodesCount = n
        self.NodeDict={}
        for i in range(n):
            self.NodeDict[i] = Node(i)
    def connect(self,a,b):
        n1 = self.NodeDict[a]
        n2 = self.NodeDict[b]
        n1.Adjesants.append(n2)
        n2.Adjesants.append(n1)
    def find_all_distances(self,s):
        srcNode = self.NodeDict[s]
        q = deque()
        q.append(srcNode)
        srcNode.destance = 0
        while q:
            vNode = q.popleft()
            if not vNode.visited:
                vNode.visited = True
                for adjNode in vNode.Adjesants:
                    dest = vNode.destance + 6
                    if adjNode.destance > dest or adjNode.destance == -1:
                        adjNode.destance = dest
                    q.append(adjNode)
        result = []
        for i in range(self.NodesCount):
            if i != s:
                result.append(str(self.NodeDict[i].destance))
            
        print(" ".join(result))