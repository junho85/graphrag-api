from fastapi import FastAPI
import uvicorn
import logging
from graphrag_api.config import config

# Configure logging
logging_config = config.get_logging_config()
logging.basicConfig(
    level=getattr(logging, logging_config.get("level", "INFO")),
    format=logging_config.get("format", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
)

# Get application configuration
app_config = config.get_app_config()
server_config = config.get_server_config()

app = FastAPI(
    title=app_config.get("title", "GraphRAG API"),
    description=app_config.get("description", "API for GraphRAG"),
    version=app_config.get("version", "0.1.0"),
)

@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(
        app, 
        host=server_config.get("host", "0.0.0.0"), 
        port=int(server_config.get("port", 8000)),
        reload=server_config.get("debug", False),
        log_level="debug" if server_config.get("debug", False) else "info",
    )
