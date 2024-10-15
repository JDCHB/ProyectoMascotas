import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.genero_mascota_model import Genero_Mascota
from fastapi.encoders import jsonable_encoder


class Genero_Mascotas_controller():

    # CREAR GENERO
    def create_genero_mascota(self, genero_mascota: Genero_Mascota):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO genero_mascota (genero, estado) VALUES (%s, %s)",
                           (genero_mascota.genero, genero_mascota.estado,))
            conn.commit()
            conn.close()
            return {"resultado": "Genero creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    # BUSCAR GENERO
    def get_genero_mascota(self, genero_mascota_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM genero_mascota WHERE id = %s", (genero_mascota_id,))
            result = cursor.fetchone()
            payload = []
            content = {}

            content = {
                'id': int(result[0]),
                'genero': result[1],
                'estado': bool(result[2]),
            }
            payload.append(content)

            json_data = jsonable_encoder(content)
            if result:
                return json_data
            else:
                raise HTTPException(
                    status_code=404, detail="Gender not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    # VER GENEROS
    def get_todos_genero_mascota(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM genero_mascota")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    'id': int(data[0]),
                    'genero': data[1],
                    'estado': bool(data[2]),
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="Gender not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    # ACTUALIZAR GENERO
    def update_genero_mascota(self, genero_mascota_id: int, genero_mascota: Genero_Mascota):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE genero_mascota SET genero = %s, estado = %s WHERE id = %s",
                (genero_mascota.genero, genero_mascota.estado, genero_mascota_id,)
            )
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(
                    status_code=404, detail="Gender not found")

            return {"mensaje": "Genero actualizado exitosamente"}

        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))

        finally:
            if conn:
                conn.close()

    # ELIMINAR GENERO
    def delete_genero_mascota(self, genero_mascota_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM genero_mascota WHERE id = %s", (genero_mascota_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(
                    status_code=404, detail="Gender not found")
            return {"mensaje": "Genero eliminado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()
