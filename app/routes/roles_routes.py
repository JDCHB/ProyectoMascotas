from fastapi import APIRouter, HTTPException
from app.models.roles_model import Roles
from app.controllers.roles_controller import *
router = APIRouter()

nuevo_rol = Rolescontroller()


@router.post("/create_rol")
async def create_rol(roles: Roles):
    rpta = nuevo_rol.create_rol(roles)
    return rpta


@router.get("/get_rol/{rol_id}", response_model=Roles)
async def get_rol(rol_id: int):
    try:
        rpta = nuevo_rol.get_rol(rol_id)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/update_rol/{rol_id}")
async def update_rol(rol_id: int, roles: Roles):
    try:
        rpta = nuevo_rol.update_rol(rol_id, roles)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get_roles/")
async def get_roles():
    rpta = nuevo_rol.get_roles()
    return rpta


@router.delete("/delete_rol/{rol_id}")
async def delete_rol(rol_id: int):
    try:
        rpta = nuevo_rol.delete_rol(rol_id)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
