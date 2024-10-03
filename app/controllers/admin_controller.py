import mysql.connector
from fastapi import HTTPException, UploadFile
import pandas as pd
from app.config.db_config import get_db_connection
from app.models.user_model import User
from app.models.mascotas_model import Mascotas
from fastapi.encoders import jsonable_encoder


class adminController:

    # Cargue Masivo
    def create_usuario_masivo(self, file: UploadFile):
        conn = None
        try:
            # Leer el archivo Excel
            df = pd.read_excel(file.file, engine='openpyxl')

            required_columns = ['email', 'password',
                                'nombre', 'apellido', 'documento', 'telefono', 'id_rol']
            for col in required_columns:
                if col not in df.columns:
                    return {"error": f"Falta la columna: {col}"}

            # Conectar a la base de datos
            conn = get_db_connection()
            cursor = conn.cursor()

            for index, row in df.iterrows():
                cursor.execute("INSERT INTO usuarios (email,password,nombre,apellido,documento,telefono,id_rol) VALUES (%s, %s, %s, %s, %s ,%s ,%s)",
                               (row['email'], row['password'],
                                row['nombre'], row['apellido'], row['documento'], row['telefono'], row['id_rol'])
                               )

            conn.commit()  # Hacer commit después de todas las inserciones
            return {"resultado": "Atributos creados exitosamente"}
        except mysql.connector.Error as err:
            if conn:
                conn.rollback()  # Asegúrate de que conn esté definido
            return {"error": str(err)}
        except Exception as e:
            if conn:
                conn.rollback()
            return {"error": f"Un error inesperado ocurrió: {str(e)}"}
        finally:
            if conn:
                conn.close()

    # HASTA AQUI

    # USUARIOS

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

    # MASCOTAS
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
# user_controller = UserController()
