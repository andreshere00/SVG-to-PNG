import os
import logging
from src.utils.config_loader import load_config

# Load configuration
config = load_config()

# Extract logging configuration
LOG_FOLDER = config.get("logging", {}).get("output_folder", "./logs")
ENABLE_LOGGING = config.get("logging", {}).get("enable", False)
LOGGING_LEVEL = config.get("logging", {}).get("level", "INFO").upper()

if ENABLE_LOGGING:
    # Ensure the log folder exists
    os.makedirs(LOG_FOLDER, exist_ok=True)

    # Configure logging
    logging.basicConfig(
        level=getattr(logging, LOGGING_LEVEL, logging.INFO),
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(os.path.join(LOG_FOLDER, "application.log")),
            logging.StreamHandler(),  # Logs to console
        ],
    )
    logger = logging.getLogger("svg_processor")
else:
    # Completely disable all logging
    logging.disable(logging.CRITICAL)
    logger = logging.getLogger("svg_processor")
    logger.addHandler(logging.NullHandler())
