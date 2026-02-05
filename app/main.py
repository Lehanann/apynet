from fastapi import FastAPI
from app.core.settings import settings
from app.api.v1.endpoints import (corporate_router, 
                                  company_router, 
                                  department_router, 
                                  service_router, 
                                  profession_router, 
                                  position_router, 
                                  employee_router, 
                                  user_account_router, 
                                  system_role_router, 
                                  material_router,
                                  phone_number_router,
                                  site_router,
                                  meeting_room_router
                                )
#from app.api.v1.endpoints.company_route import router as company_router
#from app.api.v1.endpoints.corporate_route import  router as corporate_router
#from app.api.v1.endpoints.department_route import router as department_router

from databases.postgresql import Base, engine

app = FastAPI()

app.include_router(company_router)
app.include_router(corporate_router)
app.include_router(department_router)
app.include_router(service_router)
app.include_router(profession_router)
app.include_router(position_router)
app.include_router(employee_router)
app.include_router(user_account_router)
app.include_router(system_role_router)
app.include_router(material_router)
app.include_router(phone_number_router)
app.include_router(meeting_room_router)
app.include_router(site_router)

@app.get("/")
async def root_api():
    """
    entrypoint FastApi
    :return:  welcome message
    """
    return {"Message": "Welcome Intranet API - Lehanann Corp."}