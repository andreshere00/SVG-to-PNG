import os
import yaml
from typing import Any, Optional


class ConfigLoader:
    """A class to handle loading configuration from a YAML file."""

    def __init__(self, config_path: str = "./src/config/config.yaml"):
        """
        Initialize the ConfigLoader with the path to the configuration file.

        Args:
            config_path (str): Path to the configuration file. Default is "./src/config/config.yaml".
        """
        self.config_path = config_path
        self._config_data: Optional[dict[str, Any]] = None

    def load(self) -> dict[str, Any]:
        """
        Load the configuration from the YAML file.

        Returns:
            dict: Configuration data as a dictionary.

        Raises:
            FileNotFoundError: If the configuration file does not exist.
            RuntimeError: If there is an error in parsing the YAML file.
        """
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")

        try:
            with open(self.config_path, "r", encoding="utf-8") as file:
                self._config_data = yaml.safe_load(file) or {}
                return self._config_data
        except yaml.YAMLError as e:
            raise RuntimeError(f"Error parsing configuration file: {e}")

    def get(self, key: str, default: Any = None) -> Any:
        """
        Retrieve a value from the loaded configuration data.

        Args:
            key (str): The key to retrieve.
            default: The default value to return if the key is not found.

        Returns:
            The value associated with the key, or the default value if the key is not found.
        """
        if self._config_data is None:
            self.load()

        # Explicit assertion to guarantee self._config_data is not None
        assert self._config_data is not None, "Config data should not be None after loading."

        return self._config_data.get(key, default)
