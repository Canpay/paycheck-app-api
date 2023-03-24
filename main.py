from typing import List, Optional

from pydantic import BaseModel
from db import Place
from fastapi_versioning import VersionedFastAPI, version

from fastapi import FastAPI

from routers import places

app = FastAPI()

@app.get("/")
@version(1)
async def root():
    return {"message": "Hello World"}

app.include_router(places.router)

app = VersionedFastAPI(app,
    version_format='{major}',
    prefix_format='/v{major}')