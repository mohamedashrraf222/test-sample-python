import dill as pickle
from codeflash.tracing.replay_test import get_next_arg_and_return

from app.main import main as app_main_main

functions = ['main']
trace_file_path = r"D:\personal\work\test-sample-python\codeflash.trace"

def test_app_main_main():
    for arg_val_pkl in get_next_arg_and_return(trace_file=trace_file_path, function_name="main", file_name=r"D:\personal\work\test-sample-python\app\main.py", num_to_get=256):
        args = pickle.loads(arg_val_pkl)
        ret = app_main_main()

