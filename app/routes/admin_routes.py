from fastapi import APIRouter, HTTPException, UploadFile, File
from app.controllers.admin_controller import *
from app.models.user_model import User

router = APIRouter()

nuevo_usuario = adminController()


@router.post("/create_user")
async def create_user(user: User):
    rpta = nuevo_usuario.create_user(user)
    return rpta

# CARGUE MASIVO


@router.post("/create_usuario_masivo")
async def create_usuario_masivo(file: UploadFile = File(...)):
    rpta = nuevo_usuario.create_usuario_masivo(file)  # Esto está bien
    return rpta

# FIN CARGUE MASIVO


@router.get("/get_user/{user_id}", response_model=User)
async def get_user(user_id: int):
    rpta = nuevo_usuario.get_user(user_id)
    return rpta


@router.get("/get_users/")
async def get_users():
    rpta = nuevo_usuario.get_users()
    return rpta


@router.put("/update_user/{user_id}")
async def update_user(user_id: int, user: User):
    try:
        rpta = nuevo_usuario.update_user(user_id, user)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/delete_user/{user_id}")
async def delete_user(user_id: int):
    try:
        rpta = nuevo_usuario.delete_user(user_id)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
