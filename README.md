# graphrag-api

A simple FastAPI application for GraphRAG.

## Install dependencies
```bash
uv pip install -e .
```

## Running the API
```bash
# Run the API server
python -m graphrag_api.main

# The API will be available at http://localhost:8000
# API documentation is available at http://localhost:8000/docs, http://localhost:8000/redoc
```

## Configuration

The application is configured using the `config.yaml` file in the project root. 

### Environment Variables in Configuration

You can use environment variables in the configuration file using the `${VARIABLE_NAME}` syntax. The application also supports default values using the `${VARIABLE_NAME:default_value}` syntax. For example:

```yaml
# Example config.yaml with environment variables
server:
  host: "0.0.0.0"
  port: ${API_PORT:8000}  # Will use 8000 if API_PORT is not set
  debug: false

app:
  title: "GraphRAG API"
  description: "API for GraphRAG"
  version: "0.1.0"

# Using environment variables for sensitive information
api:
  key: ${GRAPHRAG_API_KEY:demo_key}  # Will use demo_key if GRAPHRAG_API_KEY is not set
```

The application will automatically replace `${VARIABLE_NAME}` with the value of the corresponding environment variable. If the environment variable is not set and a default value is provided, it will use the default value and log this substitution.

### Using .env Files

You can also store environment variables in a `.env` file in the project root. The application will automatically load variables from this file if it exists.

Example `.env` file:
```
API_PORT=8000
GRAPHRAG_API_KEY=your_secret_api_key
```

Note: The `.env` file is ignored by Git to prevent sensitive information from being committed to the repository.
