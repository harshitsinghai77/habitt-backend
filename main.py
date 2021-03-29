import uvicorn
from fastapi import FastAPI

from habitt.config.database import database, engine
from habitt.config.settings import get_setting
from habitt.routers.deepwork import deepwork_router
from habitt.routers.user import user_router

settings = get_setting()
app = FastAPI(title=settings.APP_NAME)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(user_router, prefix=settings.API_PREFIX + "/user", tags=["User"])
app.include_router(
    deepwork_router, prefix=settings.API_PREFIX + "/deepwork", tags=["Deepwork"]
)

if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
