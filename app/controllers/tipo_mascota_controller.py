import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.tipo_mascota_model import Tipo_mascota
from fastapi.encoders import jsonable_encoder


class Tipo_Mascota_controller():

    # CREAR TIPO DE MASCOTA
    def create_tipo_mascota(self, tipo_mascota: Tipo_mascota):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tipo_mascota (tp_mascota,estado) VALUES (%s, %s)",
                           (tipo_mascota.tp_mascota, tipo_mascota.estado))
            conn.commit()
            conn.close()
            return {"resultado": "Tipo de Mascota creada"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    # BUSCAR TIPO DE MASCOTA
    def get_tipo_mascota(self, tipo_mascota_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM tipo_mascota WHERE id = %s", (tipo_mascota_id,))
            result = cursor.fetchone()
            payload = []
            content = {}

            content = {
                'id': int(result[0]),
                'tp_mascota': result[1],
                'estado': bool(result[2]),
            }
            payload.append(content)

            json_data = jsonable_encoder(content)
            if result:
                return json_data
            else:
                raise HTTPException(
                    status_code=404, detail="Tipo de mascota not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    # VER TIPOS DE MASCOTAS
    def get_todos_tipo_mascota(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tipo_mascota")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    'id': int(data[0]),
                    'tp_mascota': data[1],
                    'estado': bool(data[2])
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="Tipo de mascota not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    # ACTUALIZAR TIPO DE MASCOTA
    def update_tipo_mascota(self, tipo_mascota_id: int, tipo_mascota: Tipo_mascota):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE tipo_mascota SET tp_mascota = %s, estado = %s WHERE id = %s",
                (tipo_mascota.tp_mascota, tipo_mascota.estado, tipo_mascota_id,)
            )
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(
                    status_code=404, detail="Tipo de mascota no encontrada")

            return {"mensaje": "Tipo de mascota actualizada exitosamente"}

        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))

        finally:
            if conn:
                conn.close()

    # ELIMINAR TIPO DE MASCOTA
    def delete_tipo_mascota(self, tipo_mascota_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tipo_mascota WHERE id = %s",
                           (tipo_mascota_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(
                    status_code=404, detail="Tipo de mascota no encontrada")
            return {"mensaje": "Tipo de mascota eliminada exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()
