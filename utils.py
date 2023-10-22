

def get_trace(matrix):
    trace = 0
    for i in range(min(matrix.nrows, matrix.ncols)):
        if matrix[i, i].value is not None:
            trace += matrix[i, i].value
    return trace


def is_undirected(graph):
    """
    check that graph is undirected
    :param graph: gb.Matrix
    :return: is undirected or not
    """
    transpose = graph.T
    return graph.isequal(transpose)