from typing import List
from fastapi import APIRouter
from db import Place
from fastapi_versioning import VersionedFastAPI, version


router = APIRouter()

RequestPlace = Place.get_pydantic(exclude={"id"})
@router.post("/places/")
@version(1)
async def create_place(place: RequestPlace):
    return await Place(**place.dict()).save()

@router.get("/places/", response_model=List[Place])
@version(1)
async def get_places():
    places =  await Place.objects.all()
    return places