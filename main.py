from fastapi import FastAPI
from starlette.responses import RedirectResponse
from uvicorn import run as app_run
from src.speaksnap.pipeline.summarizer import router as summary_router

app = FastAPI()
@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

app.include_router(summary_router, prefix="/api/summary")

if __name__ == "__main__":
    app_run("main:app", host="0.0.0.0", port=8000, reload=True)#on port 8000, not 8080