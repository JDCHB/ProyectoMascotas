from fastapi import APIRouter, HTTPException
from app.models.historial_ubicaciones_model import Historial_Ubicaciones
from app.controllers.historial_ubicaciones_controller import *

router = APIRouter()

nuevo_historial_ubicaciones = Historial_Ubicaciones()


@router.post("/create_historial_ubicacion")
async def create_historial_ubicacion(historial_ubicaciones: Historial_Ubicaciones):
    rpta = nuevo_historial_ubicaciones.create_historial_ubicacion(
        historial_ubicaciones)
    return rpta


@router.get("/get_historial_ubicacion/{historial_ubicaciones_id}", response_model=Historial_Ubicaciones)
async def get_historial_ubicacion(historial_ubicaciones_id: int):
    try:
        rpta = nuevo_historial_ubicaciones.get_historial_ubicacion(
            historial_ubicaciones_id)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get_historiales_ubicaciones/")
async def get_historiales_ubicaciones():
    rpta = nuevo_historial_ubicaciones.get_historiales_ubicaciones()
    return rpta


@router.put("/update_historial_ubicacion/{historial_ubicaciones_id}")
async def update_historial_ubicacion(historial_ubicaciones_id: int, historial_ubicaciones: Historial_Ubicaciones):
    try:
        rpta = nuevo_historial_ubicaciones.update_historial_ubicacion(
            historial_ubicaciones_id, historial_ubicaciones)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/delete_historial_ubicacion/{historial_ubicaciones_id}")
async def delete_historial_ubicacion(historial_ubicaciones_id: int):
    try:
        rpta = nuevo_historial_ubicaciones.delete_historial_ubicacion(
            historial_ubicaciones_id)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
