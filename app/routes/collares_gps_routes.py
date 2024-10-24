from fastapi import APIRouter, HTTPException
from app.models.collares_gps_model import Collares_GPS
from app.controllers.genero_mascota_controller import *
router = APIRouter()

nuevo_collares_gps = Collares_GPS()


@router.post("/create_collar_gps")
async def create_collar_gps(collares_gps: Collares_GPS):
    rpta = nuevo_collares_gps.create_collar_gps(collares_gps)
    return rpta


@router.get("/get_collargps/{collargps_id}", response_model=Collares_GPS)
async def get_collargps(collargps_id: int):
    try:
        rpta = nuevo_collares_gps.get_collargps(collargps_id)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get_collaresgps/")
async def get_collaresgps():
    rpta = nuevo_collares_gps.get_collaresgps()
    return rpta


@router.put("/update_collargps/{collargps_id}")
async def update_collargps(collargps_id: int, collares_gps: Collares_GPS):
    try:
        rpta = nuevo_collares_gps.update_collargps(
            collargps_id, collares_gps)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/delete_collargps/{collargps_id}")
async def delete_collargps(collargps_id: int):
    try:
        rpta = nuevo_collares_gps.delete_collargps(collargps_id)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
