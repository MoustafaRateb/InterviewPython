from ShortestReach import Graph
inputFile =open('SampleData.txt','r')
t = int(inputFile.readline())
for i in range(t):
    n,m = [int(value) for value in inputFile.readline().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in inputFile.readline().split()]
        graph.connect(x-1,y-1) 
    s = int(inputFile.readline())
    graph.find_all_distances(s-1)