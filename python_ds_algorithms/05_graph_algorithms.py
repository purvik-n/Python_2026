"""
==========================================================
  Python DS & Algorithms — Day 5: Graph Algorithms
  Author  : Purvik
  Date    : 2026-03-14
  Topic   : Adjacency list graph, BFS, DFS, Dijkstra's,
            cycle detection, topological sort
==========================================================
"""

from collections import defaultdict, deque
import heapq


# ──────────────────────────────────────────────
#  GRAPH  (undirected & directed, weighted)
# ──────────────────────────────────────────────
class Graph:
    """
    Adjacency-list graph.
    Supports directed/undirected, weighted/unweighted.
    """

    def __init__(self, directed: bool = False):
        self.directed = directed
        self._adj: dict[object, list] = defaultdict(list)
        self.vertices: set = set()

    def add_vertex(self, v):
        self.vertices.add(v)
        if v not in self._adj:
            self._adj[v] = []

    def add_edge(self, u, v, weight: float = 1):
        self.add_vertex(u)
        self.add_vertex(v)
        self._adj[u].append((v, weight))
        if not self.directed:
            self._adj[v].append((u, weight))

    def neighbors(self, v):
        return self._adj[v]

    def __repr__(self):
        lines = [f"Graph(directed={self.directed})"]
        for v in sorted(self.vertices, key=str):
            nbrs = [f"{n}({w})" for n, w in self._adj[v]]
            lines.append(f"  {v} → {nbrs}")
        return "\n".join(lines)


# ──────────────────────────────────────────────
#  BFS  — O(V + E)
# ──────────────────────────────────────────────
def bfs(graph: Graph, start) -> list:
    """Breadth-First Search – level-order traversal."""
    visited, order, queue = set(), [], deque([start])
    visited.add(start)
    while queue:
        v = queue.popleft()
        order.append(v)
        for neighbor, _ in graph.neighbors(v):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


# ──────────────────────────────────────────────
#  DFS  — O(V + E)
# ──────────────────────────────────────────────
def dfs(graph: Graph, start, visited=None) -> list:
    """Depth-First Search – recursive."""
    if visited is None:
        visited = set()
    visited.add(start)
    order = [start]
    for neighbor, _ in graph.neighbors(start):
        if neighbor not in visited:
            order.extend(dfs(graph, neighbor, visited))
    return order


# ──────────────────────────────────────────────
#  DIJKSTRA'S  — O((V + E) log V)
# ──────────────────────────────────────────────
def dijkstra(graph: Graph, source) -> dict:
    """Shortest paths from source to all vertices (non-negative weights)."""
    dist = {v: float('inf') for v in graph.vertices}
    dist[source] = 0
    prev = {v: None for v in graph.vertices}
    heap = [(0, source)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph.neighbors(u):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(heap, (dist[v], v))

    return dist, prev


def reconstruct_path(prev: dict, source, target) -> list:
    path, node = [], target
    while node is not None:
        path.append(node)
        node = prev[node]
    path.reverse()
    return path if path[0] == source else []


# ──────────────────────────────────────────────
#  CYCLE DETECTION  (undirected) — O(V + E)
# ──────────────────────────────────────────────
def has_cycle_undirected(graph: Graph) -> bool:
    visited = set()

    def dfs_cycle(v, parent):
        visited.add(v)
        for neighbor, _ in graph.neighbors(v):
            if neighbor not in visited:
                if dfs_cycle(neighbor, v):
                    return True
            elif neighbor != parent:
                return True
        return False

    for vertex in graph.vertices:
        if vertex not in visited:
            if dfs_cycle(vertex, None):
                return True
    return False


# ──────────────────────────────────────────────
#  TOPOLOGICAL SORT  (Kahn's BFS) — O(V + E)
# ──────────────────────────────────────────────
def topological_sort(graph: Graph) -> list:
    """Only works for Directed Acyclic Graphs (DAG)."""
    in_degree = {v: 0 for v in graph.vertices}
    for v in graph.vertices:
        for neighbor, _ in graph.neighbors(v):
            in_degree[neighbor] += 1

    queue = deque([v for v, d in in_degree.items() if d == 0])
    order = []
    while queue:
        v = queue.popleft()
        order.append(v)
        for neighbor, _ in graph.neighbors(v):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != len(graph.vertices):
        raise ValueError("Graph has a cycle – topological sort not possible")
    return order


# ──────────────────────────────────────────────
#  DEMO
# ──────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  UNDIRECTED GRAPH — BFS & DFS")
    print("=" * 55)
    g = Graph(directed=False)
    edges = [(1,2),(1,3),(2,4),(2,5),(3,6),(4,7)]
    for u, v in edges:
        g.add_edge(u, v)
    print(g)
    print(f"\nBFS from 1 : {bfs(g, 1)}")
    print(f"DFS from 1 : {dfs(g, 1)}")
    print(f"Has cycle? : {has_cycle_undirected(g)}")

    print()
    print("=" * 55)
    print("  WEIGHTED DIRECTED GRAPH — DIJKSTRA'S")
    print("=" * 55)
    wg = Graph(directed=True)
    weighted_edges = [
        ('A','B',4), ('A','C',2), ('C','B',1),
        ('B','D',5), ('C','D',8), ('D','E',2), ('B','E',6)
    ]
    for u, v, w in weighted_edges:
        wg.add_edge(u, v, w)
    dist, prev = dijkstra(wg, 'A')
    print("Shortest distances from A:")
    for node in sorted(dist):
        print(f"  A → {node}: {dist[node]}")
    path = reconstruct_path(prev, 'A', 'E')
    print(f"\nShortest path A → E: {' → '.join(path)}  (cost {dist['E']})")

    print()
    print("=" * 55)
    print("  DAG — TOPOLOGICAL SORT")
    print("=" * 55)
    dag = Graph(directed=True)
    dag_edges = [('build','test'),('test','deploy'),('build','lint'),
                 ('lint','test'),('compile','build')]
    for u, v in dag_edges:
        dag.add_edge(u, v)
    print(f"Topological order: {topological_sort(dag)}")
