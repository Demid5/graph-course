from abc import ABC, abstractmethod
from undirected_graph import UndirectedGraph
from utils import is_undirected, get_trace
import graphblas as gb


class TriangleCounter(ABC):

    @abstractmethod
    def triangle_count(self, A):
        pass

    @classmethod
    def preprocessing_graph(cls, graph):
        un_graph = UndirectedGraph(graph['num_vertices'], graph['edges'])
        A = un_graph.to_graphblas()
        assert is_undirected(A)
        return A


class TriangleCounterNaive(ABC):

    def triangle_count(self, A):
        AxAxA = A.mxm(A.mxm(A))
        return int(get_trace(AxAxA) / 6)


class TriangleCounterSimple(ABC):

    def triangle_count(self, A):
        C = gb.Matrix(int, A.nrows, A.ncols)
        C(A.V) << A.mxm(A)
        sum_vals = C.reduce_scalar("sum").value
        return sum_vals / 6 if sum_vals is not None else 0


class TriangleCounterCohen(ABC):

    def triangle_count(self, A):
        C = gb.Matrix(int, A.nrows, A.ncols)
        C(A.V) << gb.select.tril(A) @ gb.select.triu(A)
        sum_vals = C.reduce_scalar("sum").value
        return sum_vals / 2 if sum_vals is not None else 0


class TriangleCounterSandia(ABC):

    def triangle_count(self, A):
        C = gb.Matrix(int, A.nrows, A.ncols)
        C(A.V) << gb.select.tril(A) @ gb.select.tril(A)
        sum_vals = C.reduce_scalar("sum").value
        return sum_vals if sum_vals is not None else 0


def calc_num_triangles_in(A):
    import numpy as np
    C = gb.Matrix(int, A.nrows, A.ncols)
    C(A.V) << A.mxm(A)
    tmp = C.reduce_columnwise("sum")
    result = dict(
        index=np.arange(tmp.size),
        value=gb.io.to_numpy(tmp) / 2
    )
    return result
