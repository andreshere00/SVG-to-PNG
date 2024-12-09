import os
import time
from functools import wraps
from datetime import datetime
from src.utils.config_loader import load_config

# Load configuration
config = load_config()
TRACE_FOLDER = config.get("logging", {}).get("output_folder", "./logs")
ENABLE_TRACING = config.get("logging", {}).get("enable", False)

if ENABLE_TRACING:
    os.makedirs(TRACE_FOLDER, exist_ok=True)

def compute_execution_time():
    """
    Decorator to compute and log the execution time of a function if tracing is enabled in the config.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not ENABLE_TRACING:
                return func(*args, **kwargs)

            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                return result
            finally:
                end_time = time.time()
                execution_time = end_time - start_time

                # Generate trace log file with timestamp
                try:
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    trace_file_name = os.path.join(TRACE_FOLDER, f"{timestamp}_trace.log")
                    with open(trace_file_name, "a") as trace_file:
                        trace_file.write(
                            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
                            f"Function '{func.__name__}' executed in {execution_time:.8f} seconds.\n"
                        )
                except Exception as e:
                    print(f"Failed to write trace log: {e}")
        return wrapper
    return decorator
