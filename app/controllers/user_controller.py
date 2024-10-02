import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.mascotas_model import Mascotas
from app.models.user_model import User
from fastapi.encoders import jsonable_encoder


class Usercontroller():
    def create_mascota(self, mascota: Mascotas):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO mascota (nombre,tipo_mascota,id_propietario,coordenadas) VALUES (%s, %s, %s, %s)",
                           (mascota.nombre, mascota.tipo_mascota, mascota.id_propietario, mascota.coordenadas))
            conn.commit()
            conn.close()
            return {"resultado": "Mascota Registrada"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

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
                    'tipo_mascota': data[2],
                    'id_propietario': int(data[3]),
                    'coordenadas': data[4],
                    'fecha_hora': data[5],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="User not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

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
                "tipo_mascota": result[2],
                "id_propietario": int(result[3]),
                "coordenadas": result[4],
                "fecha_hora": result[5],

            }
            payload.append(content)

            json_data = jsonable_encoder(content)
            if result:
                return json_data
            else:
                raise HTTPException(status_code=404, detail="User not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def update_mascota(self, mascota_id: int, mascota: Mascotas):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE mascota SET nombre = %s, tipo_mascota = %s, coordenadas = %s WHERE id = %s",
                           (mascota.nombre, mascota.tipo_mascota, mascota.coordenadas, mascota_id))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(
                    status_code=404, detail="mascota not found")
            return {"mensaje": "Datos de mascota actualizado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def delete_mascotas(self, mascota_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM mascota WHERE id = %s", (mascota_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(
                    status_code=404, detail="mascota no encontrado")
            return {"mensaje": "Mascota eliminada exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    # Actualizar Usuario
    def update_user(self, user_id: int, user: User):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE usuarios SET email = %s, password = %s, nombre = %s, apellido = %s, documento = %s, telefono = %s, id_rol = %s WHERE id = %s",
                (user.email, user.password, user.nombre, user.apellido,
                 user.documento, user.telefono, user.id_rol, user_id)
            )
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(
                    status_code=404, detail="Usuario no encontrado")

            return {"mensaje": "Usuario actualizado exitosamente"}

        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))

        finally:
            if conn:
                conn.close()
