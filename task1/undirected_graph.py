import graphblas as gb
import numpy as np


class UndirectedGraph:
    def __init__(self, num_vertices, edges):
        self.num_vertices = num_vertices
        self.graph = gb.Matrix(int, num_vertices, num_vertices)
        for (edge_from, edge_to) in edges:
            self._add_edge(edge_from, edge_to, 1)

    def _add_edge(self, vertex1, vertex2, weight):
        self.graph[vertex1, vertex2] = weight
        self.graph[vertex2, vertex1] = weight

    def to_graphblas(self):
        return self.graph
