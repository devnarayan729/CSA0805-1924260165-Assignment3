import copy
import sys
import time


rows, cols = 3, 4
bad = [[0] * cols] * rows
bad[0][1] = 7

# Correct grid: each row is a different list object.
good = [[0 for _ in range(cols)] for _ in range(rows)]
good[0][1] = 7

stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T. Nagar",
}


def show_aliasing():
    print("bad:", bad)
    print("good:", good)
    print("bad[0] is bad[1] ->", bad[0] is bad[1])
    print("good[0] is good[1] ->", good[0] is good[1])

    print("T. Nagar:", stops[(13.0418, 80.2341)])
    try:
        print(stops[[13.0418, 80.2341]])
    except TypeError as exc:
        print("List key error:", exc)


def show_copy_examples():
    original = [[1, 2], [3, 4]]
    shallow = copy.copy(original)
    deep = copy.deepcopy(original)

    shallow[0][0] = 99
    deep[0][1] = 77

    print("original:", original)
    print("shallow:", shallow)
    print("deep:", deep)

    a = [10, 20, 30]
    b = a[:]
    b[0] = 999
    print("Original list after slicing:", a)
    print("Slice copy:", b)


def compare_memory_and_speed():
    list_data = list(range(1_000_000))
    tuple_data = tuple(range(1_000_000))
    print("list size:", sys.getsizeof(list_data))
    print("tuple size:", sys.getsizeof(tuple_data))

    t0 = time.perf_counter()
    for _ in range(10):
        list_data[500_000]
    t1 = time.perf_counter()
    for _ in range(10):
        tuple_data[500_000]
    t2 = time.perf_counter()
    print("List indexing time (10 reads):", t1 - t0)
    print("Tuple indexing time (10 reads):", t2 - t1)


def tuple_mutation_example():
    record = ("station-7", [10, 20, 30])
    print("Before mutation:", record)
    record[1].append(40)
    print("After mutating the list in the tuple:", record)
    print("Tuple itself is still immutable, but its contained list is mutable.")


if __name__ == "__main__":
    show_aliasing()
    print()
    show_copy_examples()
    print()
    compare_memory_and_speed()
    print()
    tuple_mutation_example()
