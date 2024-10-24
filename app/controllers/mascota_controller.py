import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.mascotas_model import Mascotas
from fastapi.encoders import jsonable_encoder


class Mascotacontroller():

    # CREAR MASCOTA
    def create_mascota(self, mascota: Mascotas):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO mascota (nombre,id_genero_mascota,id_tipo_mascota,id_propietario,estado) VALUES (%s, %s, %s, %s, %s)",
                           (mascota.nombre, mascota.id_genero_mascota, mascota.id_tipo_mascota, mascota.id_propietario, mascota.estado))
            conn.commit()
            conn.close()
            return {"resultado": "Mascota Registrada"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    # BUSCAR MASCOTA
    def get_mascota(self, mascota_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM mascota WHERE id = %s", (mascota_id,))
            result = cursor.fetchone()
            payload = []
            content = {}

            content = {
                "id": int(result[0]),
                "nombre": result[1],
                "id_genero_mascota": int(result[2]),
                "id_tipo_mascota": int(result[3]),
                "id_propietario": int(result[4]),
                "fecha_hora": result[5],
                'estado': bool(result[6]),
            }
            payload.append(content)

            json_data = jsonable_encoder(content)
            if result:
                return json_data
            else:
                raise HTTPException(
                    status_code=404, detail="Mascota not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    # VER MASCOTAS
    def get_mascotas(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM mascota")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    'id': int(data[0]),
                    'nombre': data[1],
                    'id_genero_mascota': int(data[2]),
                    'id_tipo_mascota': int(data[3]),
                    'id_propietario': int(data[4]),
                    'fecha_hora': data[5],
                    'estado': bool(data[6]),
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="Mascota not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    # ACTUALIZAR MASCOTA
    def update_mascota(self, mascota_id: int, mascota: Mascotas):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE mascota SET nombre = %s, genero = %s, estado = %s WHERE id = %s",
                           (mascota.nombre, mascota.genero, mascota.estado, mascota_id))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(
                    status_code=404, detail="Mascota not found")
            return {"mensaje": "Datos de mascota actualizado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    # ELIMINAR MASCOTA
    def delete_mascotas(self, mascota_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM mascota WHERE id = %s", (mascota_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(
                    status_code=404, detail="Mascota no encontrada")
            return {"mensaje": "Mascota eliminada exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    # FIN MASCOTAS
