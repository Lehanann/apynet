from fastapi import FastAPI
from app.core.settings import settings
#from app.api.v1.endpoints.company_route import router as company_router
from app.api.v1.endpoints.corporate_route import  router as corporate_router

from databases.postgresql import Base, engine
app = FastAPI()

#app.include_router(company_router)
app.include_router(corporate_router)

@app.get("/")
async def root_api():
    """
    entrypoint FastApi
    :return:  welcome message
    """
    return {"Message": "Welcome Intranet API - Lehanann Corp."}