from datetime import datetime

from fastapi import FastAPI, HTTPException
from fastapi.responses import Response, HTMLResponse, FileResponse
from pydantic import BaseModel
from starlette.middleware.sessions import SessionMiddleware

from item.routers import router as item_router
from user.routers import router as user_router


app = FastAPI()
app.include_router(item_router)
app.include_router(user_router)

app.add_middleware(SessionMiddleware, secret_key="secret")


@app.get("/html")
def render_html_handler():
    content = (f"<html><body><h2>시간표</h2>"
               f"<ul><li>수학</li><li>영어</li></ul></body></html>")
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
        # headers={
        #     "Content-Disposition": "attachment; filename=pepperoni_pizza.jpeg"
        # },
    )


class NowResponse(BaseModel):
    now: datetime


@app.get(
    "/base-model",
    response_model=NowResponse,
)
def base_model_response_handler():
    now = datetime.now()
    return NowResponse(now=now)


@app.get(
    "/raise-error",
    status_code=200,
)
def raise_error_handler(error: bool = False):
    if error:
        raise HTTPException(status_code=400, detail="Error")
    return {"message": "Success"}
