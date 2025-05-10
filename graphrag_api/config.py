"""
Configuration module for GraphRAG API.
This module reads configuration from config.yaml file.
"""
import os
import yaml
from typing import Dict, Any


class Config:
    """Configuration class for GraphRAG API."""
    
    _instance = None
    _config: Dict[str, Any] = {}
    
    def __new__(cls):
        """Singleton pattern implementation."""
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._load_config()
        return cls._instance
    
    def _load_config(self):
        """Load configuration from config.yaml file."""
        config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.yaml')
        
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
        
        with open(config_path, 'r') as file:
            self._config = yaml.safe_load(file)
    
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