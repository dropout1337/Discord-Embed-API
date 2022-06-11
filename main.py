import uvicorn
import logging
from fastapi import FastAPI
from core.endpoints import api, render

logging.basicConfig(
    level=logging.INFO,
    format="\x1b[38;5;147m[\x1b[0m%(asctime)s\x1b[38;5;147m]\x1b[0m %(message)s",
    datefmt="%H:%M:%S"
)

app = FastAPI(
    docs_url=None,
    redoc_url=None,
    openapi_url=None
)

app.include_router(api)
app.include_router(render)

@app.on_event("startup")
async def startup():
    logging.info("Started the api server")

@app.on_event("shutdown")
async def startup():
    logging.info("Shutting down")

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        port=80,
        host="0.0.0.0",
        log_level="error"
    )