import numpy as np

from triangle_counter import *


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
        edges=[(0, 1), (1, 2)]
    )


def check_tasks():
    # A
    graph_A = get_simple_graph_A()
    A = TriangleCounter.preprocessing_graph(graph_A)
    triangle_count_A = 2
    assert TriangleCounterNaive().triangle_count(A) == triangle_count_A
    assert TriangleCounterSimple().triangle_count(A) == triangle_count_A
    assert TriangleCounterCohen().triangle_count(A) == triangle_count_A
    assert TriangleCounterSandia().triangle_count(A) == triangle_count_A
    num_traingles_in = calc_num_triangles_in(A)
    assert (num_traingles_in['value'] == np.array([1., 2., 1., 1., 1.])).all()
    # B
    graph_B = get_simple_graph_B()
    B = TriangleCounter.preprocessing_graph(graph_B)
    triangle_count_B = 1
    assert TriangleCounterNaive().triangle_count(B) == triangle_count_B
    assert TriangleCounterSimple().triangle_count(B) == triangle_count_B
    assert TriangleCounterCohen().triangle_count(B) == triangle_count_B
    assert TriangleCounterSandia().triangle_count(B) == triangle_count_B
    num_traingles_in = calc_num_triangles_in(B)
    assert (num_traingles_in['value'] == np.array([1., 1., 1.])).all()
    # C
    graph_C = get_simple_graph_C()
    C = TriangleCounter.preprocessing_graph(graph_C)
    triangle_count_C = 0
    assert TriangleCounterNaive().triangle_count(C) == triangle_count_C
    assert TriangleCounterSimple().triangle_count(C) == triangle_count_C
    assert TriangleCounterCohen().triangle_count(C) == triangle_count_C
    assert TriangleCounterSandia().triangle_count(C) == triangle_count_C
    num_traingles_in = calc_num_triangles_in(C)
    assert (num_traingles_in['value'] == np.array([0, 0, 0])).all()
    print("Checks passed")

