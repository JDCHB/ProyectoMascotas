from fastapi import APIRouter, HTTPException, UploadFile, File
from app.models.registro_collargps_model import NuevoCollar
from app.controllers.admin_controller import *

router = APIRouter()

nuevo_admin = AdminController()


@router.post("/create_collar")
async def create_collar(nuevocollar: NuevoCollar):
    rpta = NuevoCollar.create_collar(nuevocollar)
    return rpta
