import random
import time


def weekly_totals(readings):
    """Return weekly totals using slicing."""
    if not readings:
        return []
    totals = []
    for start in range(0, len(readings), 7):
        week = readings[start:start + 7]
        totals.append(sum(week))
    return totals


def find_max_min(readings):
    """Return (max_value, max_index, min_value, min_index)."""
    if not readings:
        return None, None, None, None
    max_value = max(readings)
    min_value = min(readings)
    max_index = readings.index(max_value)
    min_index = readings.index(min_value)
    return max_value, max_index, min_value, min_index


def moving_average_naive(readings, window=7):
    """Naive method: sum each window separately."""
    if len(readings) < window:
        return []
    return [sum(readings[i:i + window]) / window for i in range(len(readings) - window + 1)]


def moving_average_running(readings, window=7):
    """More efficient method using a running sum."""
    if len(readings) < window:
        return []
    running_sum = sum(readings[:window])
    result = [running_sum / window]
    for i in range(window, len(readings)):
        running_sum += readings[i] - readings[i - window]
        result.append(running_sum / window)
    return result


def dry_days(readings):
    """Return indices of days with zero rainfall."""
    return [index for index, value in enumerate(readings) if value == 0]


def time_moving_avg(sizes=(365, 36500, 365000), repeats=3):
    """Benchmark naive and running-sum moving averages."""
    for size in sizes:
        data = [random.randint(0, 25) for _ in range(size)]
        start = time.perf_counter()
        for _ in range(repeats):
            moving_average_naive(data)
        naive_time = time.perf_counter() - start

        start = time.perf_counter()
        for _ in range(repeats):
            moving_average_running(data)
        running_time = time.perf_counter() - start

        print(f"Size={size:>7} | naive={naive_time:.6f}s | running={running_time:.6f}s")


def demo():
    readings = [2, 5, 0, 7, 9, 0, 3, 6, 1, 8, 0, 4, 3, 2, 0, 5]
    print("Rainfall readings:", readings)
    print("Weekly totals:", weekly_totals(readings))
    print("Max/min:", find_max_min(readings))
    print("Naive moving average:", moving_average_naive(readings))
    print("Running moving average:", moving_average_running(readings))
    print("Dry days:", dry_days(readings))
    print("\nBenchmarking moving averages:")
    time_moving_avg()

    empty = []
    short = [1, 2, 3]
    print("Empty list moving average:", moving_average_running(empty))
    print("Short list moving average:", moving_average_running(short))


if __name__ == "__main__":
    demo()
