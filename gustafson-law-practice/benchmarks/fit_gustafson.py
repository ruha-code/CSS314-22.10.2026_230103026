"""Summarize weak-scaling runs, fit alpha, and plot empirical/theoretical curves."""

import argparse
import csv
import math
import statistics
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt


def read_results(path):
    grouped = defaultdict(list)
    with path.open(newline="", encoding="utf-8") as stream:
        for row in csv.DictReader(stream):
            grouped[int(row["processors"])].append(float(row["seconds"]))
    if 1 not in grouped or any(len(values) < 2 for values in grouped.values()):
        raise ValueError("results must include P=1 and at least two runs per processor count")
    return grouped


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default="benchmarks/results.csv")
    parser.add_argument("--output-dir", default="plots")
    args = parser.parse_args()
    grouped = read_results(Path(args.input))
    counts = sorted(grouped)
    mean = {p: statistics.mean(grouped[p]) for p in counts}
    sd = {p: statistics.stdev(grouped[p]) for p in counts}
    sem = {p: sd[p] / math.sqrt(len(grouped[p])) for p in counts}

    baseline = mean[1]
    speedup = {p: p * baseline / mean[p] for p in counts}
    x = [p - 1 for p in counts if p != 1]
    y = [speedup[p] - 1 for p in counts if p != 1]
    slope = sum(a * b for a, b in zip(x, y)) / sum(a * a for a in x)
    alpha = 1.0 - slope
    speedup_error = {
        p: (0.0 if p == 1 else speedup[p] * math.sqrt((sem[1] / baseline) ** 2 + (sem[p] / mean[p]) ** 2))
        for p in counts
    }

    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    summary_path = output / "summary.csv"
    with summary_path.open("w", newline="", encoding="utf-8") as stream:
        fields = ["processors", "runs", "mean_seconds", "std_seconds", "stderr_seconds",
                  "measured_speedup", "speedup_stderr", "gustafson_fit", "amdahl_fit", "ideal"]
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        for p in counts:
            writer.writerow({
                "processors": p,
                "runs": len(grouped[p]),
                "mean_seconds": f"{mean[p]:.9f}",
                "std_seconds": f"{sd[p]:.9f}",
                "stderr_seconds": f"{sem[p]:.9f}",
                "measured_speedup": f"{speedup[p]:.8f}",
                "speedup_stderr": f"{speedup_error[p]:.8f}",
                "gustafson_fit": f"{p-alpha*(p-1):.8f}",
                "amdahl_fit": f"{1/(alpha+(1-alpha)/p):.8f}" if alpha >= 0 else "",
                "ideal": f"{p:.8f}",
            })

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(counts, counts, linestyle=":", color="#555555", label="Ideal linear")
    ax.plot(counts, [p-alpha*(p-1) for p in counts], color="#0072B2",
            label=f"Gustafson fit (α={alpha:.4f})")
    if alpha >= 0:
        ax.plot(counts, [1/(alpha+(1-alpha)/p) for p in counts], linestyle="--",
                color="#D55E00", label="Amdahl, same α")
    ax.errorbar(counts, [speedup[p] for p in counts],
                yerr=[speedup_error[p] for p in counts], fmt="o", capsize=3,
                color="#009E73", label="Measured ± standard error")
    ax.set_xscale("log", base=2)
    ax.set_xlabel("Processes (P)")
    ax.set_ylabel("Scaled speedup (P × T₁ / Tₚ)")
    ax.set_title("Measured weak scaling versus theoretical models", fontweight="bold")
    ax.grid(True, which="major", alpha=0.25)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend()
    fig.tight_layout()
    fig.savefig(output / "scaling_comparison.png", dpi=300, bbox_inches="tight")
    fig.savefig(output / "scaling_comparison.pdf", bbox_inches="tight")
    plt.close(fig)

    (output / "fit_summary.txt").write_text(
        f"Least-squares fit: speedup = 1 + (1 - alpha)(P - 1)\n"
        f"alpha_observed = {alpha:.8f}\n"
        f"processor_counts = {', '.join(map(str, counts))}\n",
        encoding="utf-8",
    )
    print(f"alpha_observed={alpha:.6f}; wrote {summary_path} and scaling comparison plots.")


if __name__ == "__main__":
    main()
