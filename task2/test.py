import numpy as np

from task2.bfs_algs import *


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

def get_complex_graph():
    return dict(
        num_vertices=7,
        edges=[(3, 0), (0, 1), (3, 2), (5, 2), (6, 2), (0, 3), (6, 3), (1, 4), (6, 4), (2, 5), (4, 5), (1, 6)]
    )


def check_tasks():
    check_bfs_levels()
    check_bfs_parents()


def check_bfs_levels():
    assert bfs_level(preprocessing_graph(get_simple_graph_B())) == [(0, [0, 1, 2]), (1, [2, 0, 1]), (2, [1, 2, 0])]
    assert bfs_level(preprocessing_graph(get_simple_graph_C())) == [(0, [0, 1, 2]), (1, [-1, 0, 1]), (2, [-1, -1, 0])]
    assert bfs_level(preprocessing_graph(get_simple_graph_A())) == [
        (0, [0, 1, 2, 2, 2]),
        (1, [2, 0, 1, 1, 1]),
        (2, [1, 2, 0, 3, 3]),
        (3, [-1, -1, -1, 0, 1]),
        (4, [-1, -1, -1, -1, 0])]
    assert bfs_level(preprocessing_graph(get_complex_graph())) == [
        (0, [0, 1, 2, 1, 2, 3, 2]),
        (1, [3, 0, 2, 2, 1, 2, 1]),
        (2, [-1, -1, 0, -1, -1, 1, -1]),
        (3, [1, 2, 1, 0, 3, 2, 3]),
        (4, [-1, -1, 2, -1, 0, 1, -1]),
        (5, [-1, -1, 1, -1, -1, 0, -1]),
        (6, [2, 3, 1, 1, 1, 2, 0])]
    print("BFS levels: checks passed")


def check_bfs_parents():
    assert bfs_parent(preprocessing_graph(get_simple_graph_B())) == [(0, [-1, 0, 1]), (1, [2, -1, 1]), (2, [2, 0, -1])]
    assert bfs_parent(preprocessing_graph(get_simple_graph_C())) == [(0, [-1, 0, 1]), (1, [-2, -1, 1]),
                                                                     (2, [-2, -2, -1])]
    assert bfs_parent(preprocessing_graph(get_simple_graph_A())) == [
        (0, [-1, 0, 1, 1, 1]),
        (1, [2, -1, 1, 1, 1]),
        (2, [2, 0, -1, 1, 1]),
        (3, [-2, -2, -2, -1, 3]),
        (4, [-2, -2, -2, -2, -1])]
    assert bfs_parent(preprocessing_graph(get_complex_graph())) == [
        (0, [-1, 0, 3, 0, 1, 2, 1]),
        (1, [3, -1, 6, 6, 1, 4, 1]),
        (2, [-2, -2, -1, -2, -2, 2, -2]),
        (3, [3, 0, 3, -1, 1, 2, 1]),
        (4, [-2, -2, 5, -2, -1, 4, -2]),
        (5, [-2, -2, 5, -2, -2, -1, -2]),
        (6, [3, 0, 6, 6, 6, 2, -1])]

    print("BFS parents: checks passed")