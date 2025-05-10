"""
Test script to verify that the configuration module works correctly.
"""
from graphrag_api.config import config

def test_config():
    """Test the configuration module."""
    # Test server configuration
    server_config = config.get_server_config()
    print("Server Configuration:")
    print(f"  Host: {server_config.get('host')}")
    print(f"  Port: {server_config.get('port')}")
    print(f"  Debug: {server_config.get('debug')}")
    
    # Test application configuration
    app_config = config.get_app_config()
    print("\nApplication Configuration:")
    print(f"  Title: {app_config.get('title')}")
    print(f"  Description: {app_config.get('description')}")
    print(f"  Version: {app_config.get('version')}")
    
    # Test logging configuration
    logging_config = config.get_logging_config()
    print("\nLogging Configuration:")
    print(f"  Level: {logging_config.get('level')}")
    print(f"  Format: {logging_config.get('format')}")
    
    # Test direct access to configuration values
    print("\nDirect Access to Configuration Values:")
    print(f"  Server Host: {config.get('server', 'host')}")
    print(f"  App Title: {config.get('app', 'title')}")
    print(f"  Logging Level: {config.get('logging', 'level')}")
    
    # Test default values
    print("\nDefault Values:")
    print(f"  Non-existent Section: {config.get('non_existent', default='Default Value')}")
    print(f"  Non-existent Key: {config.get('server', 'non_existent', default='Default Value')}")

if __name__ == "__main__":
    test_config()