from task2.simple_graph import Graph
from graphblas import Matrix
from graphblas import dtypes
from graphblas import binary, semiring


def preprocessing_graph(graph):
    graph = Graph(graph['num_vertices'], graph['edges'])
    A = graph.to_graphblas()
    return A


def _preparing_result_levels(parents):
    N = parents.nrows
    result = []
    for i in range(N):
        parents_i = []
        for j in range(N):
            if i == j:
                parents_i.append(0)
                continue
            if parents[i, j].value is None:
                parents_i.append(-1)
            else:
                parents_i.append(parents[i, j].value - 1)
        result.append((i, parents_i))
    return result


def bfs_level(A):
    n = A.nrows
    result = Matrix(dtypes.INT32, n, n)  # vector for result with levels
    f = Matrix(bool, n, n)
    for i in range(n):
        f[i, i] << True

    level = 0  # level in BFS traversal
    while level < n:
        level += 1
        result(mask=f.V) << level
        f(~result.S, replace=True) << f.mxm(A, semiring.lor_land)

    return _preparing_result_levels(result)


def _preparing_result_parents(parents):
    N = parents.nrows
    result = []
    for i in range(N):
        parents_i = []
        for j in range(N):
            if i == j:
                parents_i.append(-1)
                continue
            if parents[i, j].value is None:
                parents_i.append(-2)
            else:
                parents_i.append(parents[i, j].value)
        result.append((i, parents_i))
    return result


def bfs_parent(A):
    N = A.nrows
    index_ramp = Matrix(dtypes.UINT64, N, N)
    for i in range(N):
        for j in range(N):
            index_ramp[i, j] = j

    parents = Matrix(dtypes.UINT64, N, N)
    for i in range(N):
        parents[i, i] << i

    wavefront = Matrix(dtypes.UINT64, N, N)
    for i in range(N):
        wavefront[i, i] << i

    while wavefront.nvals > 0:
        wavefront << index_ramp.ewise_mult(wavefront, binary.first)
        wavefront(~parents.S, replace=True) << wavefront.mxm(A, semiring.min_first)
        parents(binary.plus) << wavefront

    return _preparing_result_parents(parents)