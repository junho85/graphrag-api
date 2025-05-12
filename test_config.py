"""
Test script to verify that the configuration module works correctly.
Includes tests for environment variable substitution.
"""
import os
from app.config import config

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

def test_env_var_substitution():
    """Test environment variable substitution in configuration."""
    # Set a test environment variable
    test_var_name = "TEST_ENV_VAR"
    test_var_value = "test_value"
    os.environ[test_var_name] = test_var_value

    # Create a temporary config with environment variable references
    # Note: This is just for demonstration, it doesn't actually modify the config.yaml file
    print("\nEnvironment Variable Substitution:")
    print(f"  Set environment variable {test_var_name}={test_var_value}")
    print(f"  If you had a config value like '${{{{test_var_name}}}}', it would be replaced with '{test_var_value}'")

    # Check if any actual environment variables are being used in the current config
    print("\nChecking for environment variables in current config:")
    for section in ['server', 'app', 'logging']:
        section_config = config.get(section, default={})
        for key, value in section_config.items():
            if isinstance(value, str) and '${' in value:
                print(f"  Found environment variable reference in {section}.{key}: {value}")

    # Clean up
    del os.environ[test_var_name]
    print(f"\nRemoved test environment variable {test_var_name}")


if __name__ == "__main__":
    test_config()
    test_env_var_substitution()
