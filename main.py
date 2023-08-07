from fastapi import FastAPI
import uvicorn
from fastapi.routing import APIRouter
# from sqlalchemy import Column, Boolean, String
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.orm import sessionmaker, declarative_base
# import settings
# from sqlalchemy.dialects.postgresql import UUID
# import uuid
# import re
# from fastapi import HTTPException
# from pydantic import BaseModel
# from pydantic import EmailStr
# from pydantic import validator

from api.handlers import user_router

#########################
# BLOCK WITH API ROUTES #
#########################

# create instance of the app
app = FastAPI(title="luchanos-oxford-university")

# create the instance for the routes
main_api_router = APIRouter()

# set routes to the app instance
main_api_router.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(main_api_router)

if __name__ == "__main__":
    # run app on the host and port
    uvicorn.run(app, host="0.0.0.0", port=8000)
