import math
import random
from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, weight=1):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def dijkstra(self, start):
        dist = {i: math.inf for i in range(self.V)}
        dist[start] = 0
        visited = set()
        queue = deque()
        queue.append(start)

        while queue:
            u = min(queue, key=lambda vertex: dist[vertex])
            queue.remove(u)
            visited.add(u)
            for v, weight in self.graph[u]:
                if v not in visited and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    queue.append(v)
        return dist

    def prim_mst(self):
        key = [math.inf] * self.V
        parent = [-1] * self.V
        key[0] = 0
        mstSet = [False] * self.V

        for _ in range(self.V):
            u = min((k for k in range(self.V) if not mstSet[k]), key=lambda x: key[x])
            mstSet[u] = True
            for v, weight in self.graph[u]:
                if not mstSet[v] and weight < key[v]:
                    key[v] = weight
                    parent[v] = u
        result = []
        for i in range(1, self.V):
            result.append((parent[i], i, key[i]))
        return result

def generate_random_graph(vertices, edges):
    g = Graph(vertices)
    added = set()
    while len(added) < edges:
        u = random.randint(0, vertices - 1)
        v = random.randint(0, vertices - 1)
        if u != v and (u, v) not in added and (v, u) not in added:
            weight = random.randint(1, 20)
            g.add_edge(u, v, weight)
            added.add((u, v))
    return g

def main():
    vertices = 10
    edges = 15
    graph = generate_random_graph(vertices, edges)

    dist = graph.dijkstra(0)
    print("Distâncias mais curtas a partir do vértice 0:")
    for vertex in range(vertices):
        print(f"Vértice {vertex}: {dist[vertex]}")

    mst = graph.prim_mst()
    print("\nÁrvore Geradora Mínima (arestas e seus pesos):")
    for u, v, weight in mst:
        print(f"{u} - {v} : {weight}")

if __name__ == "__main__":
    main()
