import uvicorn
import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def helloworld():
    await asyncio.sleep(0.2)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)