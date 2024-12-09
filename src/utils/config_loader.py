import yaml
import os

def load_config(config_path: str = "./src/config/config.yaml") -> dict:
    """
    Loads the configuration from a YAML file.

    Args:
        config_path (str): Path to the configuration file. Default is "./config/config.yaml".

    Returns:
        dict: Configuration data as a dictionary.

    Raises:
        FileNotFoundError: If the configuration file does not exist.
        yaml.YAMLError: If there is an error in parsing the YAML file.
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    try:
        with open(config_path, "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)
            return config   

    except yaml.YAMLError as e:
        raise RuntimeError(f"Error parsing configuration file: {e}")
