from fastapi import APIRouter, HTTPException, UploadFile, File
from app.models.admin_model import NuevoCollar
from app.controllers.admin_controller import *

router = APIRouter()

nuevo_admin = AdminController()


@router.post("/create_collar")
async def create_collar(nuevocollar: NuevoCollar):
    rpta = nuevo_admin.create_collar(nuevocollar)
    return rpta


@router.post("/create_rol")
async def create_rol(nuevorol: NuevoRol):
    rpta = nuevo_admin.create_rol(nuevorol)
    return rpta
