"""
Configuration module for GraphRAG API.
This module reads configuration from config.yaml file.
Supports environment variable substitution using ${VAR_NAME} syntax.
Also loads environment variables from .env file if it exists.
"""
import os
import re
import yaml
import logging
from typing import Dict, Any, Union

# Try to import dotenv, but don't fail if it's not installed
try:
    from dotenv import load_dotenv
    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False


class Config:
    """Configuration class for GraphRAG API."""

    _instance = None
    _config: Dict[str, Any] = {}
    _env_pattern = re.compile(r'\${([A-Za-z0-9_:]+)}')

    def __new__(cls):
        """Singleton pattern implementation."""
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._load_env_vars()
            cls._instance._load_config()
        return cls._instance

    def _load_env_vars(self):
        """Load environment variables from .env file if it exists."""
        if DOTENV_AVAILABLE:
            # Look for .env file in the project root directory
            env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
            if os.path.exists(env_path):
                load_dotenv(env_path)

    def _substitute_env_vars(self, value: Any) -> Any:
        """
        Substitute environment variables in configuration values.

        Args:
            value: Configuration value to process

        Returns:
            Processed configuration value with environment variables substituted
        """
        if isinstance(value, str):
            # Replace ${VAR_NAME} or ${VAR_NAME:default_value} with environment variable value
            def replace_env_var(match):
                env_var_expr = match.group(1)
                
                # Check if there's a default value specified (using : as separator)
                if ':' in env_var_expr:
                    env_var_name, default_value = env_var_expr.split(':', 1)
                else:
                    env_var_name = env_var_expr
                    default_value = None
                
                env_var_value = os.environ.get(env_var_name)
                
                if env_var_value is not None:
                    return env_var_value
                elif default_value is not None:
                    logging.info(f"Environment variable '{env_var_name}' not found, using default value: {default_value}")
                    return default_value
                else:
                    logging.warning(f"Environment variable '{env_var_name}' not found and no default value provided")
                    return match.group(0)

            return self._env_pattern.sub(replace_env_var, value)
        elif isinstance(value, dict):
            # Process nested dictionaries
            return {k: self._substitute_env_vars(v) for k, v in value.items()}
        elif isinstance(value, list):
            # Process lists
            return [self._substitute_env_vars(item) for item in value]
        else:
            # Return other types unchanged
            return value

    def _load_config(self):
        """Load configuration from config.yaml file and substitute environment variables."""
        config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.yaml')

        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file not found: {config_path}")

        with open(config_path, 'r') as file:
            config_data = yaml.safe_load(file)
            # Substitute environment variables in configuration values
            self._config = self._substitute_env_vars(config_data)

    def get(self, section: str, key: str = None, default: Any = None) -> Any:
        """
        Get configuration value.

        Args:
            section: Configuration section
            key: Configuration key within section (optional)
            default: Default value if key is not found (optional)

        Returns:
            Configuration value or default
        """
        if section not in self._config:
            return default

        if key is None:
            return self._config[section]

        if key not in self._config[section]:
            return default

        return self._config[section][key]

    def get_server_config(self) -> Dict[str, Any]:
        """Get server configuration."""
        return self.get('server', default={})

    def get_app_config(self) -> Dict[str, Any]:
        """Get application configuration."""
        return self.get('app', default={})

    def get_logging_config(self) -> Dict[str, Any]:
        """Get logging configuration."""
        return self.get('logging', default={})


# Create a singleton instance
config = Config()
