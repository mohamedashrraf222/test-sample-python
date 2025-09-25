import math

import pytest

from app.processing import DataProcessor, moving_average, sanitize_numbers, summarize


def test_sanitize_numbers_coerces_and_ignores():
    values = ["1", 2, 3.5, None, " ", "4.5"]
    assert sanitize_numbers(values) == [1.0, 2.0, 3.5, 4.5]


def test_sanitize_numbers_raises_on_bad_value():
    with pytest.raises(ValueError):
        sanitize_numbers(["abc"])  # cannot parse


def test_moving_average_prefix_behavior():
    seq = [1.0, 2.0, 3.0, 4.0]
    assert moving_average(seq, 3) == [1.0, 1.5, 2.0, 3.0]


def test_summarize_empty():
    assert summarize([]) == (None, None, None)


def test_processor_pipeline_and_normalization():
    dp = DataProcessor.from_raw([1, 2, 3, 4])
    norm = dp.normalize_0_1()
    assert norm.values == [0.0, 1/3, 2/3, 1.0]
    ma = norm.with_moving_average(2)
    assert ma.values == [0.0, (0.0 + 1/3)/2, (1/3 + 2/3)/2, (2/3 + 1.0)/2]
    vmin, vmean, vmax = ma.summary()
    assert pytest.approx(vmin, rel=1e-9) == 0.0
    assert pytest.approx(vmax, rel=1e-9) == 0.8333333333333334
    assert pytest.approx(vmean, rel=1e-9) == sum(ma.values) / len(ma.values)


