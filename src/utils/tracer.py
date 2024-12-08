import os
import time
from functools import wraps
from datetime import datetime
from src.utils.config_loader import load_config

config = load_config()
TRACE_FOLDER = config.get("trace_folder", "./logs")
ENABLE_TRACING = config.get("enable_tracing", False)

if ENABLE_TRACING:
    os.makedirs(TRACE_FOLDER, exist_ok=True)

def compute_execution_time():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not ENABLE_TRACING:
                return func(*args, **kwargs)
            
            print(f"Tracing enabled. Logging execution time for {func.__name__}")
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                return result
            finally:
                end_time = time.time()
                execution_time = end_time - start_time
                try:
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    trace_file_name = os.path.join(TRACE_FOLDER, f"{timestamp}.log")
                    with open(trace_file_name, "a") as trace_file:
                        trace_file.write(
                            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
                            f"Function '{func.__name__}' executed in {execution_time:.8f} seconds.\n"
                        )
                    print(f"Execution time logged in: {trace_file_name}")
                except Exception as e:
                    print(f"Failed to write trace log: {e}")
        return wrapper
    return decorator
