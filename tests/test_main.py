from app.main import main, run_pipeline, flatten_numbers_arg


def test_flatten_numbers_arg():
    assert flatten_numbers_arg(["1,2", "3", "4,5,6"]) == ["1", "2", "3", "4", "5", "6"]


def test_run_pipeline_basic():
    out = run_pipeline(["1", "2", "3", "4"], window=2, normalize=False)
    assert "count=4" in out
    assert "min=1.0" in out
    assert "max=4.0" in out


def test_main_returns_output_string():
    result = main(["1", "2", "3", "--window", "2"])  # prints and returns
    assert "count=3" in result

