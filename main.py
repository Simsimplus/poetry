# This is a sample Python script.
import uvicorn

from route import app

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
