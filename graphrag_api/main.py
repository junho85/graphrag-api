from fastapi import FastAPI

app = FastAPI(
    title="GraphRAG API",
    description="API for GraphRAG",
    version="0.1.0",
)

@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)