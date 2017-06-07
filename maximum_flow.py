# python 3
# http://practice.geeksforgeeks.org/problems/find-the-maximum-flow/0
# FordFulkerson + Undirected graph

import collections
import sys

class FlowEdge:
    flow = 0

    def __init__(self, s, t, capacity):
        self.source = s
        self.target = t
        self.capacity = capacity

    def __repr__(self):
        represents = "(Source: %d, Target: %d, Capacity: %d, Flow: %d)"%(self.source, self.target, self.capacity, self.flow)
        return represents

    def getResidualCapacity(self, flowTo):
        if flowTo == self.source: # backward, this is different point from directed graph
            return self.capacity + self.flow
        elif flowTo == self.target: # forward
            return self.capacity - self.flow
        else:
            raise Error("Error")

    def addFlow(self, flowTo, flow):
        if flowTo == self.source:
            self.flow -= flow
        elif flowTo == self.target:
            self.flow += flow
        else:
            raise Error("Error")

    def getSource(self):
        return self.source
    
    def getTarget(self):
        return self.target

    def getOther(self, point):
        if point == self.source:
            return self.target
        elif point == self.target:
            return self.source
        else:
            raise Error("Error")

class FlowNetwork:
    def __init__(self, numVertex):
        self.n = numVertex
        self.adjacentList = [[] for _ in range(numVertex)]

    def addEdge(self, src, target, capacity):
        if src == target:
            return
        presents = self.getEdge(src, target)
        if presents is not None:
            presents.capacity += capacity
            return
        
        reverse_presents = self.getEdge(target, src)
        if reverse_presents is not None:
            reverse_presents.capacity += capacity
            return
        
        edge = FlowEdge(src, target, capacity)
        self.adjacentList[src].append(edge)
        self.adjacentList[target].append(edge)
    
    def getEdges(self, vertex):
        return self.adjacentList[vertex]

    def getEdge(self, src, dst):
        for edge in self.adjacentList[src]:
            if edge.getSource() == dst and edge.getTarget() == src:
                return edge
            if edge.getTarget() == dst:
                return edge
        return None

    def __repr__(self):
        represents = "Vertex: %d, List: %s"%(self.n, self.adjacentList)
        return represents

class Graph:
    def __init__(self, graph):
        self.graph = graph

    def BFS(self, src, target, parent):
        visited = [False] * self.graph.n

        # queue for breadth first search
        queue = collections.deque()
        queue.append(src)
        visited[src] = True

        while queue:
            vertex = queue.popleft()

            # Get all adjacent vertex
            for edge in self.graph.getEdges(vertex):
                t = edge.getOther(vertex)
                if visited[t] == False and edge.getResidualCapacity(t) > 0:
                    queue.append(t)
                    visited[t] = True
                    parent[t] = vertex

        return visited[target]

    def EdmondsKarp(self, source, sink):
        maxFlow = 0
        parentList = [-1] * self.graph.n

        while self.BFS(source, sink, parentList):
            pathFlow = sys.maxsize
            s = sink

            # compute min flow
            while s != source:
                parent = parentList[s]
                edge = self.graph.getEdge(parent, s)
                pathFlow = min(pathFlow, edge.getResidualCapacity(s))
                s = parent
            maxFlow += pathFlow
            # update residual capacities
            v = sink
            while v != source:
                u = parentList[v]
                edge = self.graph.getEdge(u, v)
                edge.addFlow(v, pathFlow)
                v = u
        return maxFlow
    
if __name__ == "__main__":
    num_cases = int(input())
    # num_cases = 1
    results = []
    for _ in range(num_cases):
        # str_input = "10 20"
        str_input = input()
        splitted = str_input.split(' ')
        n = int(splitted[0])
        m = int(splitted[1])

        # create flow list
        flow_graph = FlowNetwork(n)
        
        # complete flow list
        # str_input = "1 2 1 3 2 2 4 2 3 2 5 5"
        # str_input = "1 2 8 1 3 10 2 4 2 3 4 3"
        # str_input = "1 2 1000 1 3 1000 2 3 1 2 4 1000 3 4 1000"
        # str_input = "1 6 9 3 2 7 6 1 7 5 1 2 5 3 2 5 4 5 3 2 8 2 2 8 3 5 9 2 3 3 "
        # str_input = "5 7 8 6 3 2 9 3 1 5 6 10 7 8 8 1 9 5 5 2 7 4 6 10 10 7 1 4 3 1 5 4 8 6 3 3 4 1 8 1 2 1 4 8 4 5 5 10 2 6 9 6 10 4 10 9 6 8 1 4 "
        str_input = input()
        splitted = str_input.split(' ')
        for i in range(m):
            idx_base = 3 * i
            src = int(splitted[idx_base]) - 1 
            dst = int(splitted[idx_base+1]) - 1
            capacity = int(splitted[idx_base+2])

            flow_graph.addEdge(src, dst, capacity)
        # print("Graph: ", flow_graph)
        graph = Graph(flow_graph)
        results.append(graph.EdmondsKarp(0, n-1))
    
    for result in results:
        print(result)

