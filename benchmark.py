import time
import graphblas as gb
import glob

import numpy as np

from triangle_counter import *
import matplotlib.pyplot as plt


def triangle_count(A, method='sandia'):
    if method == "naive":
        return TriangleCounterNaive().triangle_count(A)
    elif method == "simple":
        return TriangleCounterSimple().triangle_count(A)
    elif method == "cohen":
        return TriangleCounterCohen().triangle_count(A)
    elif method == "sandia":
        return TriangleCounterSandia().triangle_count(A)
    else:
        raise Exception(f"Unexpected method {method}")


def benchmark():
    methods = ['naive', 'simple', 'cohen', 'sandia']
    sizes = []
    times = dict()
    for method in methods:
        times[method] = []
    for filepath in glob.iglob('data/*.mtx'):
        A = gb.io.mmread(filepath)
        sizes.append(A.ncols)
        for method in methods:
            start_time = time.perf_counter()
            triangle_count(A, method)
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            times[method].append(execution_time)
            print(f"Method: {method}, time: {execution_time}")
        print("______________")

    sortinds = np.argsort(sizes)
    for method in methods:
        plt.plot(np.array(sizes)[sortinds], np.log(np.array(times[method])[sortinds]), label=method)
    plt.xlabel("number of columns")
    plt.ylabel("log(time)")
    plt.legend()
    plt.show()