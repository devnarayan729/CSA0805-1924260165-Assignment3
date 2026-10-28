import sys
import time


def clean_loop(readings):
    cleaned = []
    for value in readings:
        if -50 <= value <= 50:
            cleaned.append(value)
    return cleaned


def clean_comprehension(readings):
    return [value for value in readings if -50 <= value <= 50]


def clean_map_filter(readings):
    return list(filter(lambda value: -50 <= value <= 50, readings))


def alarm_minutes(readings):
    return [minute for minute, temp in enumerate(readings) if temp < 2 or temp > 8]


def dict_and_set_examples(readings):
    valid_count = len(clean_loop(readings))
    invalid_count = len(readings) - valid_count
    print("valid_count:", valid_count)
    print("invalid_count:", invalid_count)
    print("alarm_minutes:", alarm_minutes(readings))
    print("dict comprehension:", {"valid": valid_count, "invalid": invalid_count})
    print("set comprehension:", {minute for minute, value in enumerate(readings) if value < 2 or value > 8})


if __name__ == "__main__":
    readings = [12, 5, 9, -55, 7, 45, 52, -10, 3, 2, 8, 67, 32]
    loop_result = clean_loop(readings)
    comp_result = clean_comprehension(readings)
    map_filter_result = clean_map_filter(readings)

    print("Loop result:", loop_result)
    print("Comprehension result:", comp_result)
    print("Map/filter result:", map_filter_result)
    print("All results identical:", loop_result == comp_result == map_filter_result)

    print("Alarm minutes:", alarm_minutes(readings))
    dict_and_set_examples(readings)

    for size in (10_000, 100_000, 1_000_000):
        sample = [((i % 20) - 10) for i in range(size)]
        t0 = time.perf_counter(); clean_loop(sample); t1 = time.perf_counter()
        t2 = time.perf_counter(); clean_comprehension(sample); t3 = time.perf_counter()
        t4 = time.perf_counter(); clean_map_filter(sample); t5 = time.perf_counter()
        print(f"size={size:>7} | loop={t1-t0:.6f}s | comp={t3-t2:.6f}s | map_filter={t5-t4:.6f}s")

    list_comp = [x * 2 for x in range(100_000)]
    gen_expr = (x * 2 for x in range(100_000))
    print("list_comprehension_memory:", sys.getsizeof(list_comp))
    print("generator_expression_memory:", sys.getsizeof(gen_expr))
