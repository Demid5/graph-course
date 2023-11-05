from task3.shortest_path_finders import *


def get_simple_graph_A():
    return dict(
        num_vertices=5,
        edges=[(0, 1, 3), (1, 2, 5), (2, 0, 8), (3, 4, 1), (1, 3, 1), (1, 4, -2)]
    )


def get_simple_graph_B():
    return dict(
        num_vertices=3,
        edges=[(0, 1, 1), (1, 2, 6), (2, 0, 9)]
    )


def get_complex_graph():
    return dict(
        num_vertices=7,
        edges=[
            (3, 0, 3),
            (0, 1, 2),
            (3, 2, 3),
            (5, 2, 1),
            (6, 2, 5),
            (0, 3, 3),
            (6, 3, 7),
            (1, 4, 8),
            (6, 4, 3),
            (2, 5, 1),
            (4, 5, 7),
            (1, 6, 4)
        ]
    )


def check_bellman_ford_multi():
    assert bellman_ford_multi(preprocessing_graph(get_simple_graph_B()), [1, 2]) == [(1, [15, 0, 6]), (2, [9, 10, 0])]
    assert bellman_ford_multi(preprocessing_graph(get_simple_graph_A()), [0, 3, 4]) == [
        (0, [0, 3, 8, 4, 1]),
        (3, [float('inf'), float('inf'), float('inf'), 0, 1]),
        (4, [float('inf'), float('inf'), float('inf'), float('inf'), 0])]
    assert bellman_ford_multi(preprocessing_graph(get_complex_graph()), [1, 2, 3]) == [
        (1, [14, 0, 9, 11, 7, 10, 4]),
        (2, [float('inf'), float('inf'), 0, float('inf'), float('inf'), 1, float('inf')]),
        (3, [3, 5, 3, 0, 12, 4, 9])]
    print("Bellman Ford multi: checks passed")


def check_transitive_closure_and_floyd_warshall():
    answ_B = [(0, [0, 1, 7]), (1, [15, 0, 6]), (2, [9, 10, 0])]
    assert floyd_warshall(preprocessing_graph(get_simple_graph_B())) == answ_B
    assert transitive_closure(preprocessing_graph(get_simple_graph_B())) == answ_B
    answ_A = [
        (0, [0, 3, 8, 4, 1]),
        (1, [13, 0, 5, 1, -2]),
        (2, [8, 11, 0, 12, 9]),
        (3, [float('inf'), float('inf'), float('inf'), 0, 1]),
        (4, [float('inf'), float('inf'), float('inf'), float('inf'), 0])]
    assert floyd_warshall(preprocessing_graph(get_simple_graph_A())) == answ_A
    assert transitive_closure(preprocessing_graph(get_simple_graph_A())) == answ_A
    answ_complex = [
        (0, [0, 2, 6, 3, 9, 7, 6]),
        (1, [14, 0, 9, 11, 7, 10, 4]),
        (2, [float('inf'), float('inf'), 0, float('inf'), float('inf'), 1, float('inf')]),
        (3, [3, 5, 3, 0, 12, 4, 9]),
        (4, [float('inf'), float('inf'), 8, float('inf'), 0, 7, float('inf')]),
        (5, [float('inf'), float('inf'), 1, float('inf'), float('inf'), 0, float('inf')]),
        (6, [10, 12, 5, 7, 3, 6, 0])]
    assert floyd_warshall(preprocessing_graph(get_complex_graph())) == answ_complex
    assert transitive_closure(preprocessing_graph(get_complex_graph())) == answ_complex
    print("Transitive closure and Floyd Warshall: checks passed")


def check_bellman_ford_single():
    assert bellman_ford_single(preprocessing_graph(get_simple_graph_A()), 3) == [float('inf'), float('inf'), float('inf'), 0, 1]
    assert bellman_ford_single(preprocessing_graph(get_simple_graph_B()), 2) == [9, 10, 0]
    assert bellman_ford_single(preprocessing_graph(get_complex_graph()), 1) == [14, 0, 9, 11, 7, 10, 4]
    assert bellman_ford_single(preprocessing_graph(get_complex_graph()), 4) == [float('inf'), float('inf'), 8, float('inf'), 0, 7, float('inf')]

    print("Bellman Ford single: checks passed")


def check_tasks():
    check_bellman_ford_single()
    check_bellman_ford_multi()
    check_transitive_closure_and_floyd_warshall()

