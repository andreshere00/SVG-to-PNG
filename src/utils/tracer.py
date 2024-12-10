import os
import time
from functools import wraps

from src.utils.config_loader import ConfigLoader


class Tracer:
    """Handle function execution time tracing."""

    def __init__(self, config_path: str = "./src/config/config.yaml", logger=None):
        """
        Initialize the tracer class.

        Args:
            config_path (str): Path to the configuration file. Default is "./src/config/config.yaml".
            logger (logging.Logger, optional): Logger instance for logging. If None, tracing will be disabled.
        """
        config_loader = ConfigLoader(config_path)
        config = config_loader.load()

        self.enable_tracing = config.get("logging", {}).get("enable", False)
        self.trace_folder = config.get("logging", {}).get("output_folder", "./logs")
        self.logger = logger

        if self.enable_tracing:
            os.makedirs(self.trace_folder, exist_ok=True)

    def compute_execution_time(self, func):
        """Compute and log the execution time of a function."""

        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                return func(*args, **kwargs)
            finally:
                end_time = time.time()
                execution_time = end_time - start_time
                if self.logger and self.enable_tracing:
                    self.logger.info(
                        f"Function '{func.__name__}' executed in {execution_time:.8f} seconds."
                    )

        return wrapper
