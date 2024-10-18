from fastapi import APIRouter
from model import model
from service import list_service

listde_router = APIRouter(
  prefix="/listde"
)

list_service = list_service.ListDEService()

@listde_router.get("/")
async def get_kids_list():
    return list_service.get_kids()

@listde_router.post("/add")
async def add_kid_to_final(data: model.Kid):
    list_service.add_kid(data)
    return {"message": "Adicionado exitosamente"}

@listde_router.post("/tostart")
async def add_kid_to_start(data: model.Kid):
    list_service.add_kid_to_start(data)
    return {"message": "Adicionado exitosamente"}

# Añadir un niño en una posición específica
@listde_router.post("/inposition/{position}")
async def add_kid_in_position(data: model.Kid, position: int):
    if position < 1 or position > list_service.get_size():
        return {"message": "Posición no válida"}
    list_service.add_kid_in_position(data, position)
    return {"message": "Adicionado exitosamente"}

@listde_router.post("/invert")
async def invert_kids_list():
    list_service.invert()
    return {"message": "Lista invertida exitosamente"}

@listde_router.delete("/deleteid/{id_delete}")
async def delete_kid_by_id(id_delete: str):
    list_service.delete_kid_by_id(id_delete)
    return {"message": "Eliminado exitosamente"}

@listde_router.delete("/deletepst/{position}")
async def delete_kid_by_position(position: int):
    if position < 1 or position > list_service.get_size():
        return {"message": "Posición no válida"}
    list_service.delete_kid_by_position(position)
    return {"message": "Eliminado exitosamente"}

@listde_router.get("/mixbygender")
async def mix_by_gender():
    list_service.switch_by_gender()
    return {"message": "Lista intercalada por género"}

# Intercambiar los extremos de la lista
@listde_router.post("/switchends")
async def switch_kids_list_ends():
    list_service.switch_ends()
    return {"message": "Extremos intercambiandos exitosamente"}