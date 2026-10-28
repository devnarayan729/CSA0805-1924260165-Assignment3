import random
import time


def build_timetable(train_count=5):
    timetable = {}
    for i in range(1, train_count + 1):
        train_no = f"{12000 + i}"
        timetable[train_no] = {
            "name": f"Train {train_no}",
            "stops": [
                ("Chennai", "08:00", "08:15"),
                ("Vellore", "09:10", "09:20"),
                ("Bengaluru", "11:00", "11:15"),
                ("Mysuru", "13:00", "13:10"),
            ],
            "days": {"Mon", "Wed", "Fri"},
        }
    return timetable


def query_without_index(timetable, station, day):
    matches = []
    for train_no, info in timetable.items():
        for stop in info["stops"]:
            if stop[0] == station and day in info["days"]:
                matches.append((train_no, stop[2]))
    return matches


def build_station_index(timetable):
    index = {}
    for train_no, info in timetable.items():
        for station, arrival, departure in info["stops"]:
            index.setdefault(station, []).append((train_no, departure, info["days"]))
    return index


def query_with_index(index, station, day):
    matches = []
    for train_no, departure, days in index.get(station, []):
        if day in days:
            matches.append((train_no, departure))
    return matches


def benchmark_queries():
    for size in (100, 1000, 10_000):
        timetable = build_timetable(size)
        index = build_station_index(timetable)
        station = "Bengaluru"
        day = "Wed"

        t0 = time.perf_counter(); query_without_index(timetable, station, day); t1 = time.perf_counter()
        t2 = time.perf_counter(); query_with_index(index, station, day); t3 = time.perf_counter()
        print(f"size={size:>5} | without_index={t1-t0:.6f}s | with_index={t3-t2:.6f}s | index_size={len(index)}")


if __name__ == "__main__":
    timetable = build_timetable(5)
    print("Timetable:")
    for train_no, info in timetable.items():
        print(train_no, info)

    print("\nTrains stopping at Bengaluru on Wed without index:", query_without_index(timetable, "Bengaluru", "Wed"))
    station_index = build_station_index(timetable)
    print("Trains stopping at Bengaluru on Wed with index:", query_with_index(station_index, "Bengaluru", "Wed"))
    print("Unknown station:", query_with_index(station_index, "Unknown", "Mon"))

    print("\nBenchmark:")
    benchmark_queries()
