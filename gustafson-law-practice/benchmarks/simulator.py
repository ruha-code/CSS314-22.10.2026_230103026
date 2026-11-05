"""Compare strong (Amdahl) and weak (Gustafson) scaling."""

import argparse
import csv
from pathlib import Path

import matplotlib.pyplot as plt


DEFAULT_CORES = [2**power for power in range(17)]
DEFAULT_ALPHAS = [0.001, 0.01, 0.04, 0.10, 0.20]


def parse_numbers(value, cast):
    return [cast(item.strip()) for item in value.split(",") if item.strip()]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cores", default=",".join(map(str, DEFAULT_CORES)))
    parser.add_argument("--alphas", default=",".join(map(str, DEFAULT_ALPHAS)))
    parser.add_argument("--output-dir", default="benchmarks")
    args = parser.parse_args()

    cores = sorted(set(parse_numbers(args.cores, int)))
    alphas = sorted(set(parse_numbers(args.alphas, float)))
    if not cores or any(p < 1 or p > 65536 for p in cores):
        parser.error("processor counts must be in the range 1..65536")
    if not alphas or any(a < 0.001 or a > 0.20 for a in alphas):
        parser.error("serial fractions must be in the range 0.001..0.20")

    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    csv_path = output / "simulator_results.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as stream:
        fields = ["processors", "serial_fraction", "amdahl_speedup", "gustafson_speedup",
                  "amdahl_efficiency", "gustafson_efficiency"]
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        for alpha in alphas:
            for p in cores:
                amdahl = 1.0 / (alpha + (1.0 - alpha) / p)
                gustafson = p - alpha * (p - 1)
                writer.writerow({
                    "processors": p,
                    "serial_fraction": f"{alpha:.6f}",
                    "amdahl_speedup": f"{amdahl:.8f}",
                    "gustafson_speedup": f"{gustafson:.8f}",
                    "amdahl_efficiency": f"{amdahl / p:.8f}",
                    "gustafson_efficiency": f"{gustafson / p:.8f}",
                })

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), sharex=True)
    palette = plt.get_cmap("tab10")
    for index, alpha in enumerate(alphas):
        color = palette(index % 10)
        strong = [1.0 / (alpha + (1.0 - alpha) / p) for p in cores]
        weak = [p - alpha * (p - 1) for p in cores]
        axes[0].plot(cores, strong, marker="o", ms=3, color=color, label=f"α={alpha:g}")
        axes[1].plot(cores, weak, marker="o", ms=3, color=color, label=f"α={alpha:g}")
    ideal = cores
    for ax in axes:
        ax.plot(cores, ideal, color="#555555", linestyle="--", linewidth=1, label="Ideal")
        ax.set_xscale("log", base=2)
        ax.set_yscale("log")
        ax.set_xlabel("Processors (P)")
        ax.set_ylabel("Speedup (log scale)")
        ax.spines[["top", "right"]].set_visible(False)
        ax.legend(fontsize=8)
    axes[0].set_title("Amdahl: fixed workload")
    axes[1].set_title("Gustafson: scaled workload")
    fig.suptitle("Strong and weak scaling across processor counts", fontweight="bold")
    fig.tight_layout()
    fig.savefig(output / "simulator_comparison.png", dpi=300, bbox_inches="tight")
    fig.savefig(output / "simulator_comparison.pdf", bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote {csv_path} and comparison plots ({len(cores)} processor counts, {len(alphas)} fractions).")


if __name__ == "__main__":
    main()
