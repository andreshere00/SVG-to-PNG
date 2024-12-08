import os
import logging
from src.utils.config_loader import load_config

# Load configuration
config = load_config()
LOG_FOLDER = config.get("trace_folder", "./logs")
ENABLE_LOGGING = config.get("enable_logging", False)
LOGGING_LEVEL = config.get("logging_level", "INFO").upper()

if ENABLE_LOGGING:
    os.makedirs(LOG_FOLDER, exist_ok=True)

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
