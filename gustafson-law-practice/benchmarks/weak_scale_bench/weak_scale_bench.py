"""CPU-bound weak-scaling benchmark using Python multiprocessing."""

import argparse
import csv
import math
import multiprocessing as mp
import os
import statistics
import time
from pathlib import Path


def work(item):
    worker_id, work_items = item
    offset = worker_id * work_items
    total = 0.0
    for index in range(work_items):
        value = math.sin((offset + index + 1) * 0.001)
        total += value * value
    return total


def parse_counts(value):
    counts = sorted(set(int(part.strip()) for part in value.split(",") if part.strip()))
    maximum = os.cpu_count() or 1
    if not counts or counts[0] < 1 or counts[-1] > maximum:
        raise argparse.ArgumentTypeError(f"thread counts must be between 1 and {maximum}")
    return counts


def run_configuration(processes, work_items, runs):
    tasks = [(worker_id, work_items) for worker_id in range(processes)]
    records = []
    with mp.Pool(processes=processes) as pool:
        pool.map(work, tasks)  # warm-up; pool startup is outside timed runs
        for run_number in range(1, runs + 1):
            start = time.perf_counter()
            checksum = sum(pool.map(work, tasks))
            elapsed = time.perf_counter() - start
            records.append({
                "processors": processes,
                "run": run_number,
                "seconds": f"{elapsed:.9f}",
                "work_items_per_process": work_items,
                "checksum": f"{checksum:.12f}",
            })
    return records


def main():
    maximum = os.cpu_count() or 1
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--thread-counts", type=parse_counts,
                        default=list(range(1, maximum + 1)))
    parser.add_argument("--work-items", type=int, default=100_000)
    parser.add_argument("--runs", type=int, default=5)
    parser.add_argument("--output", default="benchmarks/results.csv")
    args = parser.parse_args()
    if args.work_items < 1 or args.runs < 2:
        parser.error("work-items must be positive and runs must be at least 2")

    records = []
    for processes in args.thread_counts:
        records.extend(run_configuration(processes, args.work_items, args.runs))
        times = [float(row["seconds"]) for row in records if row["processors"] == processes]
        print(f"P={processes}: mean={statistics.mean(times):.6f}s, "
              f"sd={statistics.stdev(times):.6f}s ({len(times)} runs)")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as stream:
        fields = ["processors", "run", "seconds", "work_items_per_process", "checksum"]
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(records)
    print(f"Saved raw measurements to {output} ({len(records)} rows).")


if __name__ == "__main__":
    mp.freeze_support()
    main()
