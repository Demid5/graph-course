import graphblas as gb
from graphblas import Matrix, Vector
from graphblas import unary, binary, monoid, semiring, dtypes
from simple_graph import Graph


def preprocessing_graph(graph):
    graph = Graph(graph['num_vertices'], graph['edges'])
    A = graph.to_graphblas()
    return A


def pagerank_3f(graph, damping=0.85, itermax=100, tol=1e-4):
    A = preprocessing_graph(graph)
    A << A.apply(unary.one)
    d_out = A.reduce_rowwise(monoid.plus).new()
    return pagerank_3f_impl(A, d_out, damping, itermax, tol)


def pagerank_3f_impl(A, d_out, damping=0.85, itermax=100, tol=1e-4):
    """
    Returns (result as Vector, iters as int)
    """
    n = A.nrows
    teleport = (1 - damping) / n
    rdiff = 1  # first iteration is always done

    # r = 1 / n
    t = Vector(dtypes.FP32, n)
    r = Vector(dtypes.FP32, n)
    w = Vector(dtypes.FP32, n)
    r[:] << 1.0 / n

    # prescale with damping factor, so it isn't done each iteration
    # d = d_out / damping
    d = d_out.dup(dtype="FP32")
    d(accum=binary.truediv)[:] << damping

    # --------------------------------------------------------------------------
    # pagerank iterations
    # --------------------------------------------------------------------------
    for i in range(itermax):
        if rdiff <= tol:
            break

        # swap t and r ; now t is the old score
        r, t = t, r

        # w = t ./ d
        w << t.ewise_mult(d, binary.truediv)

        # r = teleport
        r[:] << teleport

        # r += A'*w
        r(binary.plus) << A.T.mxv(w, semiring.plus_second)

        # t -= r
        t(binary.minus)[:] << r

        # t = abs (t)
        t << t.apply(unary.abs)

        # rdiff = sum (t)
        rdiff = t.reduce(monoid.plus).value

    return [r[i].value for i in range(r.size)]




