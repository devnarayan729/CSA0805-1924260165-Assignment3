import time


ai_elective = {"192311001", "192311004", "192311007", "192311009"}
iot_elective = {"192311002", "192311004", "192311009", "192311010"}
all_students = {f"1923110{i:02d}" for i in range(1, 11)}

both = ai_elective & iot_elective
exactly_one = (ai_elective | iot_elective) - both
neither = all_students - (ai_elective | iot_elective)

print("clash      :", sorted(both))
print("exactlyone:", sorted(exactly_one))
print("neither   :", sorted(neither))


def set_method_version():
    both2 = ai_elective.intersection(iot_elective)
    exactly_one2 = ai_elective.symmetric_difference(iot_elective)
    neither2 = all_students.difference(ai_elective.union(iot_elective))
    print("set method clash      :", sorted(both2))
    print("set method exactlyone:", sorted(exactly_one2))
    print("set method neither   :", sorted(neither2))


def membership_benchmark():
    for size in (10_000, 100_000, 1_000_000):
        xs = list(range(size))
        ys = set(xs)
        target = size // 2

        t0 = time.perf_counter()
        target in xs
        list_time = time.perf_counter() - t0

        t0 = time.perf_counter()
        target in ys
        set_time = time.perf_counter() - t0

        print(f"n={size:>7} | list membership={list_time:.8f}s | set membership={set_time:.8f}s")


if __name__ == "__main__":
    set_method_version()
    print()
    membership_benchmark()
