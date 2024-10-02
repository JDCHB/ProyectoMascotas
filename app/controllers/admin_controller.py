import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.user_model import User
from fastapi.encoders import jsonable_encoder


class adminController:

    def create_user(self, user: User):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (email,password,nombre,apellido,documento,telefono,id_rol) VALUES (%s, %s, %s, %s, %s ,%s ,%s)",
                           (user.email, user.password, user.nombre, user.apellido, user.documento, user.telefono, user.id_rol))
            conn.commit()
            conn.close()
            return {"resultado": "Usuario creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def get_user(self, user_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
            result = cursor.fetchone()
            payload = []
            content = {}

            content = {
                'id': int(result[0]),
                'email': result[1],
                'password': result[2],
                'nombre': result[3],
                'apellido': result[4],
                'documento': result[5],
                'telefono': result[6],
                'id_rol': int(result[7])
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

    def get_users(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    'id': int(data[0]),
                    'email': data[1],
                    'password': data[2],
                    'nombre': data[3],
                    'apellido': data[4],
                    'documento': data[5],
                    'telefono': data[6],
                    'id_rol': int(data[7])
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

    # Editar usuario
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

    def delete_user(self, user_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM usuarios WHERE id = %s", (user_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(
                    status_code=404, detail="Usuario no encontrado")
            return {"mensaje": "Usuario eliminado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()


# user_controller = UserController()
