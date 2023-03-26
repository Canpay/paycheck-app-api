from typing import Any, List
from fastapi import APIRouter
from ormar import NoMatch
from pydantic import ValidationError
from db import Place
from fastapi_versioning import VersionedFastAPI, version
from fastapi.responses import JSONResponse

router = APIRouter()

RequestPlace = Place.get_pydantic(exclude={"id"})
@router.post("/places/")
@version(1)
async def create_place(place: RequestPlace):
    return await Place(**place.dict()).save()

@router.get("/places/", response_model=List[Place])
@version(1)
async def get_places():
    try:
        places =  await Place.objects.all()
    except AssertionError as e:
        print("Exception getting places: " + str(e))
    return places

@router.put("/places/{place_id}", response_model=None)
async def update_place(place_id: int, up_gourmet_check: bool) -> Any:
    try:
        place = await Place.objects.get(id=place_id)
    except NoMatch as e:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
    
    place_updated = await place.update(up_gourmet_check = up_gourmet_check)
    return place_updated
