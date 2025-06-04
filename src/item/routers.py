from fastapi import APIRouter, UploadFile
from fastapi.params import Query, Path, Body
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1/items", tags=["Item"])


# 1) Path 변수
@router.get("/{item_id}")
def get_item_handler(item_id: int = Path(ge=1)):
    return {"message": item_id}


# 2) Query Parameter
@router.get("")
def get_items_handler(
    max_price: int = Query(ge=100, lt=1000, default=100)
):
    return {"max_price": max_price}

# 3) Request Body
class ItemCreateRequest(BaseModel):
    name: str


@router.post("")
def create_item_handler(
    body: ItemCreateRequest,
    # name: str = Body(embed=True)
):
    return {"name": body.name}
    # return {"name": name}


# 4) Multi-Part Form
@router.post("/{item_id}/images")
def upload_item_image_handler(image: UploadFile):
    return {
        "filename": image.filename,
        "content_type": image.content_type,
        "size": image.size,
    }
