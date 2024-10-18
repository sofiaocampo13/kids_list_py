from fastapi import FastAPI
from controller.list_controller import listde_router

app = FastAPI()

app.include_router(listde_router)
