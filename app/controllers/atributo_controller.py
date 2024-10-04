import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.atributo_model import Atributo
from fastapi.encoders import jsonable_encoder


class Atributocontroller():

    # CREAR ATRIBUTO
    def create_atributo(self, atributo: Atributo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO atributo (nombre, descripcion) VALUES (%s, %s)",
                           (atributo.nombre, atributo.descripcion,))
            conn.commit()
            conn.close()
            return {"resultado": "Atributo creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    # BUSCAR ATRIBUTO
    def get_atributo(self, atributo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM atributo WHERE id = %s", (atributo_id,))
            result = cursor.fetchone()
            payload = []
            content = {}

            content = {
                'id': int(result[0]),
                'nombre': result[1],
                'descripcion': result[2],

            }
            payload.append(content)

            json_data = jsonable_encoder(content)
            if result:
                return json_data
            else:
                raise HTTPException(
                    status_code=404, detail="Atributo not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    # VER USUARIOS
    def get_atributos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM atributo")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    'id': int(data[0]),
                    'nombre': data[1],
                    'descripcion': data[2],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="Atributos not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    # ACTUALIZAR ATRIBUTO
    def update_atributo(self, atributo_id: int, atributo: Atributo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE atributo SET nombre = %s, descripcion = %s WHERE id = %s",
                (atributo.nombre, atributo.descripcion, atributo_id)
            )
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(
                    status_code=404, detail="Atributo no encontrado")

            return {"mensaje": "Atributo actualizado exitosamente"}

        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))

        finally:
            if conn:
                conn.close()

    # ELIMINAR USARIO
    def delete_atributo(self, atributo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM atributo WHERE id = %s", (atributo_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(
                    status_code=404, detail="Atributo no encontrado")
            return {"mensaje": "Atributo eliminado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()
