import dill as pickle
from codeflash.tracing.replay_test import get_next_arg_and_return

from app.main import evaluate_guess as app_main_evaluate_guess
from app.main import game_loop as app_main_game_loop
from app.main import get_user_guess as app_main_get_user_guess
from app.main import main as app_main_main
from app.main import print_welcome_message as app_main_print_welcome_message

functions = ['main', 'print_welcome_message', 'game_loop', 'get_user_guess', 'evaluate_guess']
trace_file_path = r"D:\personal\work\test-sample-python\codeflash.trace"

def test_app_main_main():
    for arg_val_pkl in get_next_arg_and_return(trace_file=trace_file_path, function_name="main", file_name=r"D:\personal\work\test-sample-python\app\main.py", num_to_get=256):
        args = pickle.loads(arg_val_pkl)
        ret = app_main_main()

def test_app_main_print_welcome_message():
    for arg_val_pkl in get_next_arg_and_return(trace_file=trace_file_path, function_name="print_welcome_message", file_name=r"D:\personal\work\test-sample-python\app\main.py", num_to_get=256):
        args = pickle.loads(arg_val_pkl)
        ret = app_main_print_welcome_message()

def test_app_main_game_loop():
    for arg_val_pkl in get_next_arg_and_return(trace_file=trace_file_path, function_name="game_loop", file_name=r"D:\personal\work\test-sample-python\app\main.py", num_to_get=256):
        args = pickle.loads(arg_val_pkl)
        ret = app_main_game_loop()

def test_app_main_get_user_guess():
    for arg_val_pkl in get_next_arg_and_return(trace_file=trace_file_path, function_name="get_user_guess", file_name=r"D:\personal\work\test-sample-python\app\main.py", num_to_get=256):
        args = pickle.loads(arg_val_pkl)
        ret = app_main_get_user_guess()

def test_app_main_evaluate_guess():
    for arg_val_pkl in get_next_arg_and_return(trace_file=trace_file_path, function_name="evaluate_guess", file_name=r"D:\personal\work\test-sample-python\app\main.py", num_to_get=256):
        args = pickle.loads(arg_val_pkl)
        ret = app_main_evaluate_guess(**args)

