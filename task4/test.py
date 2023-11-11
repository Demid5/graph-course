import numpy as np
from pagerank import *


def get_simple_graph_A():
    return dict(
        num_vertices=5,
        edges=[(0, 1), (1, 2), (2, 0), (3, 4), (1, 3), (1, 4)]
    )


def get_simple_graph_B():
    return dict(
        num_vertices=3,
        edges=[(0, 1), (1, 2), (2, 0)]
    )


def get_simple_graph_C():
    return dict(
        num_vertices=3,
        edges=[(0, 1), (1, 2), (0, 2)]
    )

def get_complex_graph():
    return dict(
        num_vertices=5,
        edges=[
            (0, 1),
            (0, 2),
            (1, 3),
            (2, 3),
            (2, 4),
            (3, 4),
            (4, 0)
        ]
    )


def check_task():
    complex_res = pagerank_3f(get_complex_graph())
    assert complex_res[0] > complex_res[1] and \
           complex_res[0] > complex_res[2] and \
           complex_res[4] > complex_res[1] and \
           complex_res[4] > complex_res[2]
    

    B_res = pagerank_3f(get_simple_graph_B())
    eps = 0.00001
    assert np.abs(B_res[0] - B_res[1]) < eps and \
           np.abs(B_res[0] - B_res[2]) < eps and \
           np.abs(B_res[2] - B_res[1]) < eps

    C_res = pagerank_3f(get_simple_graph_C())
    assert C_res[2] > C_res[0] and C_res[2] > C_res[1]

    A_res = pagerank_3f(get_simple_graph_A())
    assert A_res[4] > A_res[2] and A_res[4] > A_res[3]

    print("Check passed")