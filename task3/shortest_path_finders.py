from task3.simple_graph import Graph
from graphblas import Matrix
from graphblas import Vector
from graphblas import dtypes
from graphblas import binary, semiring, op


def preprocessing_graph(graph):
    graph = Graph(graph['num_vertices'], graph['edges'])
    A = graph.to_graphblas()
    return A


def bellman_ford_single(m, s):
    for i in range(m.nrows):
        m[i, i] << 0
    v = Vector(m.dtype, m.nrows)
    v[s] << 0
    while True:
        w = v.dup()
        v << v.vxm(m, semiring.min_plus)
        if v.isequal(w):
            break
    return [v[i].value if v[i].value is not None else float('inf') for i in range(v.size)]


def post_processing(v, ss):
    result = []
    for i in range(v.nrows):
        lengths_i = []
        for j in range(v.ncols):
            if v[i, j].value is None:
                lengths_i.append(float('inf'))
            else:
                lengths_i.append(v[i, j].value)
        result.append((ss[i], lengths_i))
    return result


def bellman_ford_multi(m, ss):
    for i in range(m.nrows):
        m[i, i] << 0
    v = Matrix(m.dtype, len(ss), m.nrows)
    for (i, s) in enumerate(ss):
        v[i, s] << 0
    while True:
        w = v.dup()
        v << v.mxm(m, semiring.min_plus)
        if v.isequal(w):
            break

    return post_processing(v, ss)


def floyd_warshall(m):
    d = m.dup()
    for i in range(d.nrows):
        d[i, i] << 0
    for k in range(m.ncols):
        d(accum=op.min) << d[:, [k]].mxm(d[[k], :], semiring.min_plus)

    return post_processing(d, list(range(m.ncols)))


def transitive_closure(m):
    ident = Matrix(m.dtype, m.nrows, m.nrows)
    for i in range(m.nrows):
        m[i, i] << 0
        ident[i, i] << 1
    d = ident.dup()
    v = ident.dup()
    for k in range(m.ncols):
        d << d.mxm(m, semiring.min_plus)
        v(accum=op.min) << d

    # post processing
    for i in range(m.nrows):
        for j in range(m.nrows):
            if v[i, j].value is not None:
                v[i, j] << v[i, j].value - 1

    return post_processing(v, list(range(m.ncols)))

