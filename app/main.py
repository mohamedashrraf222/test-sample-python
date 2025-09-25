# app/main.py

import argparse
from typing import List

from app.processing import DataProcessor, sanitize_numbers


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run a non-interactive numeric processing pipeline."
    )
    parser.add_argument(
        "numbers",
        nargs="*",
        help="Numbers to process (e.g. 1 2 3 4 or '1,2,3').",
    )
    parser.add_argument(
        "--window",
        type=int,
        default=3,
        help="Moving average window size (default: 3)",
    )
    parser.add_argument(
        "--normalize",
        action="store_true",
        help="Normalize values to [0,1] before summarizing.",
    )
    return parser.parse_args(argv)


def flatten_numbers_arg(numbers_args: List[str]) -> List[str]:
    flat: List[str] = []
    for token in numbers_args:
        parts = [p for p in token.split(",") if p != ""]
        flat.extend(parts)
    return flat


def run_pipeline(raw_numbers: List[str], window: int, normalize: bool) -> str:
    cleaned = sanitize_numbers(raw_numbers)
    processor = DataProcessor(values=cleaned)
    if normalize:
        processor = processor.normalize_0_1()
    processor = processor.with_moving_average(window)
    vmin, vmean, vmax = processor.summary()
    return (
        f"count={len(processor.values)} min={vmin} mean={vmean} max={vmax} "
        f"values={processor.values}"
    )


def main(argv: List[str] | None = None) -> str:
    args = parse_args(argv or [])
    flat = flatten_numbers_arg(args.numbers)
    output = run_pipeline(flat, window=args.window, normalize=args.normalize)
    print(output)
    return output


if __name__ == "__main__":
    main()