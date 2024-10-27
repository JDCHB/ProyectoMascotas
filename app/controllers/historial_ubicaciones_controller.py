import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.historial_ubicaciones_model import Historial_Ubicaciones
from fastapi.encoders import jsonable_encoder


class Historial_UbicacionesController():

    # CREAR HISTORIAL
    def create_historial_ubicacion(self, historial_ubicaciones: Historial_Ubicaciones):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO historial_ubicaciones (id_collar,latitud,longitud,distancia_recorrida) VALUES (%s, %s, %s, %s)",
                           (historial_ubicaciones.id_collar, historial_ubicaciones.latitud, historial_ubicaciones.longitud, historial_ubicaciones.distancia_recorrida))
            conn.commit()
            conn.close()
            return {"resultado": "Historial Registrado"}
        except mysql.connector.Error as err:
            # (SI VUELVE A FALLAR ACTIVEN ESTO XD) print(f"Error durante la inserción: {err}")
            conn.rollback()
        finally:
            conn.close()

    # BUSCAR HISTORIAL
    def get_historial_ubicacion(self, historial_ubicaciones_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM historial_ubicaciones WHERE id = %s", (historial_ubicaciones_id,))
            result = cursor.fetchone()
            payload = []
            content = {}

            content = {
                "id": int(result[0]),
                "id_collar": int(result[1]),
                "latitud": result[2],
                "longitud": result[3],
                "fecha_hora": result[4],
                "distancia_recorrida": result[5]
            }
            payload.append(content)

            json_data = jsonable_encoder(content)
            if result:
                return json_data
            else:
                raise HTTPException(
                    status_code=404, detail="Historial not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    # VER HISTORIALES
    def get_historiales_ubicaciones(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM historial_ubicaciones")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    "id": int(data[0]),
                    "id_collar": int(data[1]),
                    "latitud": data[2],
                    "longitud": data[3],
                    "fecha_hora": data[4],
                    "distancia_recorrida": data[5]
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="Historial not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    # ACTUALIZAR HISTORIAL
    def update_historial_ubicacion(self, historial_ubicaciones_id: int, historial_ubicaciones: Historial_Ubicaciones):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE historial_ubicaciones SET id_collar = %s, latitud = %s, longitud = %s, distancia_recorrida=%s WHERE id = %s",
                           (historial_ubicaciones.id_collar, historial_ubicaciones.latitud, historial_ubicaciones.longitud, historial_ubicaciones.distancia_recorrida, historial_ubicaciones_id))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(
                    status_code=404, detail="Historial not found")
            return {"mensaje": "Datos del historial actualizados exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    # ELIMINAR HISTORIAL
    def delete_historial_ubicacion(self, historial_ubicaciones_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM historial_ubicaciones WHERE id = %s",
                           (historial_ubicaciones_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(
                    status_code=404, detail="Historial no encontrado")
            return {"mensaje": "Historial eliminado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    # FIN HISTOTIAL DE UBICACIONES
