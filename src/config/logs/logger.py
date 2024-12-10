import logging
import os
from src.utils.config_loader import ConfigLoader
from threading import Lock


class LoggerManager:
    """A class to manage the logging configuration as a singleton."""

    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        """Ensure only one instance of LoggerManager is created."""

        with cls._lock:
            if cls._instance is None:
                cls._instance = super(LoggerManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, config_path: str = "./src/config/config.yaml"):
        """
        Initialize the logger based on configuration settings.

        Args:
            config_path (str): Path to the configuration file. Default is "./src/config/config.yaml".
        """

        if not hasattr(self, "initialized"):
            self.initialized = True
            config_loader = ConfigLoader(config_path)
            config = config_loader.load()

            self.log_folder = config.get("logging", {}).get("output_folder", "./logs")
            self.enable_logging = config.get("logging", {}).get("enable", False)
            self.logging_level = config.get("logging", {}).get("level", "INFO").upper()

            self.logger = self._setup_logger()

    def _setup_logger(self):
        """
        Set up and configure the logger based on the settings.

        Returns:
            logging.Logger: Configured logger instance.
        """

        if self.enable_logging:
            # Ensure the log folder exists
            os.makedirs(self.log_folder, exist_ok=True)

            # Configure logging
            logging.basicConfig(
                level=getattr(logging, self.logging_level, logging.INFO),
                format="%(asctime)s - %(levelname)s - %(message)s",
                handlers=[
                    logging.FileHandler(os.path.join(self.log_folder, "application.log")),
                    logging.StreamHandler(),  # Logs to console
                ],
            )
            return logging.getLogger("svg_processor")
        else:
            # Disable logging completely
            logging.disable(logging.CRITICAL)
            logger = logging.getLogger("svg_processor")
            logger.addHandler(logging.NullHandler())
            return logger
