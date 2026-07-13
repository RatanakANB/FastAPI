from fastapi import FastAPI

# Initialize the FastAPI application
app = FastAPI()

@app.get("/")
def read_root():
    """Basic root endpoint returning JSON data."""
    return {"message": "Hello from fastapiframe!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """Example endpoint accepting path and query parameters."""
    return {"item_id": item_id, "query": q}
