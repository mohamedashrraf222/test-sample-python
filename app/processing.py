import math
from dataclasses import dataclass
from typing import Iterable, List, Optional, Sequence, Tuple


def sanitize_numbers(values: Iterable[object]) -> List[float]:
    """Coerce an iterable of arbitrary objects into a clean list of floats.

    - Ignores None and NaN values
    - Parses numeric strings
    - Raises ValueError if a value cannot be coerced
    """
    cleaned: List[float] = []
    for value in values:
        if value is None:
            continue
        if isinstance(value, (int, float)):
            number = float(value)
        elif isinstance(value, str):
            value = value.strip()
            if value == "":
                continue
            try:
                number = float(value)
            except ValueError as exc:
                raise ValueError(f"Cannot parse number from string: '{value}'") from exc
        else:
            raise ValueError(f"Unsupported value type: {type(value).__name__}")

        if math.isnan(number):
            continue
        cleaned.append(number)

    return cleaned


def moving_average(values: Sequence[float], window_size: int) -> List[float]:
    """Compute a simple moving average over the sequence.

    Returns a list of the same length, with leading positions filled by None-equivalent
    smoothing (i.e., average over the available prefix for the first windows).
    """
    if window_size <= 0:
        raise ValueError("window_size must be positive")
    n = len(values)
    if n == 0:
        return []

    result: List[float] = []
    running_sum = 0.0
    for i, val in enumerate(values):
        running_sum += val
        if i >= window_size:
            running_sum -= values[i - window_size]
            avg = running_sum / window_size
        else:
            avg = running_sum / (i + 1)
        result.append(avg)
    return result


def summarize(values: Sequence[float]) -> Tuple[Optional[float], Optional[float], Optional[float]]:
    """Return (min, mean, max) for the sequence, or (None, None, None) if empty."""
    if not values:
        return None, None, None
    v_min = min(values)
    v_max = max(values)
    v_mean = sum(values) / len(values)
    return v_min, v_mean, v_max


@dataclass
class DataProcessor:
    """High-level processor for numeric datasets with useful methods."""

    values: List[float]

    @classmethod
    def from_raw(cls, raw_values: Iterable[object]) -> "DataProcessor":
        return cls(values=sanitize_numbers(raw_values))

    def with_moving_average(self, window_size: int) -> "DataProcessor":
        return DataProcessor(values=moving_average(self.values, window_size))

    def summary(self) -> Tuple[Optional[float], Optional[float], Optional[float]]:
        return summarize(self.values)

    def normalize_0_1(self) -> "DataProcessor":
        """Normalize values to [0, 1]. If constant or empty, returns zeros or empty."""
        if not self.values:
            return DataProcessor(values=[])
        v_min = min(self.values)
        v_max = max(self.values)
        span = v_max - v_min
        if span == 0:
            return DataProcessor(values=[0.0 for _ in self.values])
        return DataProcessor(values=[(v - v_min) / span for v in self.values])


