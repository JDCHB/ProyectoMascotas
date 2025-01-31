from fastapi import APIRouter, HTTPException
from app.models.admin_model import NuevoCollar, NuevoModulo
from app.controllers.admin_controller import *

router = APIRouter()

nuevo_admin = AdminController()


@router.post("/create_collar")
async def create_collar(nuevocollar: NuevoCollar):
    rpta = nuevo_admin.create_collar(nuevocollar)
    return rpta


@router.post("/create_modulo")
async def create_modulo(nuevomodulo: NuevoModulo):
    rpta = nuevo_admin.create_modulo(nuevomodulo)
    return rpta
