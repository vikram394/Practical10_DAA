class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
            return True
        return False  


def kruskal_mst(vertices, edges):
    """
    Finds the Minimum Spanning Tree (MST) using Kruskal's algorithm.
    :param vertices: List of vertices, e.g., ['A', 'B', 'C', 'D']
    :param edges: List of tuples (weight, u, v)
    :return: List of edges included in the MST, and the total weight
    """
    sorted_edges = sorted(edges, key=lambda edge: edge[0])

    dsu = DisjointSet(vertices)
    mst = []
    total_weight = 0
    for weight, u, v in sorted_edges:
        if dsu.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

            if len(mst) == len(vertices) - 1:
                break

    return mst, total_weight


if __name__ == "__main__":
    graph_vertices = ['A', 'B', 'C', 'D', 'E', 'F']

    graph_edges = [
        (4, 'A', 'B'), (4, 'A', 'C'),
        (2, 'B', 'C'), (3, 'B', 'D'), (2, 'B', 'E'),
        (3, 'C', 'E'), (4, 'D', 'E'), (5, 'D', 'F'),
        (1, 'E', 'F')
    ]

    mst_edges, min_cost = kruskal_mst(graph_vertices, graph_edges)

    print("Edges in the Minimum Spanning Tree:")
    for u, v, w in mst_edges:
        print(f"{u} -- {v} == Weight: {w}")
    print(f"Total Minimum Cost: {min_cost}")
