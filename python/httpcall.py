import uvicorn
import aiohttp
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def helloworld():
    async with aiohttp.ClientSession() as sess:
        async with sess.get("https://postman-echo.com/get?foo1=bar1&foo2=bar2") as resp:
            return await resp.text()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)