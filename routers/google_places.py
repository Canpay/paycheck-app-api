from fastapi import APIRouter
from pydantic import BaseModel
from fastapi_versioning import VersionedFastAPI, version

router = APIRouter()

@router.get("/google_places/")
@version(1)
async def get_places(latitude: float, longitude: float, radius: int):
    print("Funciona el endpoint")
   