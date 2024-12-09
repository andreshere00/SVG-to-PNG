import os
import time
from datetime import datetime
from functools import wraps

from src.utils.config_loader import ConfigLoader


class Tracer:
    """Handle function execution time tracing."""

    def __init__(self, config_path: str = "./src/config/config.yaml"):
        """
        Initialize the tracer class.

        Args:
            config_path (str): Path to the configuration file. Default is "./src/config/config.yaml".
        """
        config_loader = ConfigLoader(config_path)
        config = config_loader.load()

        self.enable_tracing = config.get("logging", {}).get("enable", False)
        self.trace_folder = config.get("logging", {}).get("output_folder", "./logs")

        if self.enable_tracing:
            os.makedirs(self.trace_folder, exist_ok=True)

    @staticmethod
    def compute_execution_time(func):
        """Compute and log the execution time of a function."""

        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                return func(*args, **kwargs)
            finally:
                end_time = time.time()
                execution_time = end_time - start_time
                print(f"Function '{func.__name__}' executed in {execution_time:.8f} seconds.")

        return wrapper
