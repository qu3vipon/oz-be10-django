from datetime import datetime

from fastapi import FastAPI
from fastapi.responses import Response, HTMLResponse, FileResponse
from pydantic import BaseModel

from item.routers import router as item_router
from user.routers import router as user_router


app = FastAPI()
app.include_router(item_router)
app.include_router(user_router)


@app.get("/html")
def render_html_handler():
    content = f"<html><body><h2> now: {datetime.now()} </h2></body></html>"
    return HTMLResponse(content)

@app.get("/plain-text")
def plain_text_handler():
    content = "Hello World!"
    return Response(content=content, media_type="text/plain")

@app.get("/images")
def image_download_handler():
    image_path = "images/pizza.jpeg"
    return FileResponse(
        path=image_path,
        headers={
            "Content-Disposition": "attachment; filename=pepperoni_pizza.jpeg"
        },
    )


class NowResponse(BaseModel):
    now: datetime


@app.get("/base-model")
def base_model_response_handler() -> NowResponse:
    now = datetime.now()
    return NowResponse(now=now)
