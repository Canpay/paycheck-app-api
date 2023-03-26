from typing import List, Optional
from db import database
from fastapi_versioning import VersionedFastAPI, version

from fastapi import FastAPI

from routers import google_places, places

app = FastAPI()

@app.get("/")
@version(1)
async def root():
    return {"message": "Hello World"}

app.include_router(places.router, tags=["places"])
app.include_router(google_places.router, tags=["google_places"])

app = VersionedFastAPI(app,
    version_format='{major}',
    prefix_format='/v{major}')

@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()