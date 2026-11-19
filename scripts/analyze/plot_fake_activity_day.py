"""Plot one day of activity for one fictional NHANES participant."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--activity",
        type=Path,
        default=REPO_ROOT / "tests/fixtures/dhlc_phase1/activity.csv",
    )
    parser.add_argument("--seqn", type=int, default=10001)
    parser.add_argument("--day", type=int, default=1)
    parser.add_argument(
        "--output",
        type=Path,
        default=REPO_ROOT / "tests/fixtures/dhlc_phase1/participant_10001_day1.png",
    )
    args = parser.parse_args()

    activity = pd.read_csv(args.activity)
    day = activity.loc[
        (activity["SEQN"] == args.seqn) & (activity["PAXDAY"] == args.day)
    ].sort_values(["PAXN"])
    if day.empty:
        raise ValueError(f"No activity found for SEQN={args.seqn} on PAXDAY={args.day}.")

    fig, ax = plt.subplots(figsize=(10, 4.5))
    ax.plot(day["PAXHOUR"], day["PAXINTEN"], marker="o", linewidth=2, color="#5AA6B3")
    ax.set(
        title=f"Fictional participant {args.seqn}: activity on day {args.day}",
        xlabel="Hour of day",
        ylabel="PAXINTEN",
        xlim=(0, 23),
    )
    ax.set_xticks(range(0, 24, 2))
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, dpi=180)
    print(args.output)


if __name__ == "__main__":
    main()
