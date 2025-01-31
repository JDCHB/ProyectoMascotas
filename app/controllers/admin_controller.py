import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.admin_model import NuevoCollar, NuevoRol, NuevoModulo
from fastapi.encoders import jsonable_encoder


class AdminController():

    # CREAR NUEVO COLLAR GPS
    def create_collar(self, nuevocollar: NuevoCollar):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Verifica si el número de serie ya existe
            cursor.execute(
                "SELECT id FROM collares_con_gps WHERE numero_serie = %s", (nuevocollar.numero_serie,))
            if cursor.fetchone():
                return {"error": "El número de serie ya está registrado."}

            # Inserta el nuevo collar
            cursor.execute(
                """
                INSERT INTO collares_con_gps (numero_serie, id_mascota_vinculada, nivel_bateria, estado)
                VALUES (%s, %s, %s, %s)
                """,
                (nuevocollar.numero_serie,
                 nuevocollar.id_mascota_vinculada, nuevocollar.nivel_bateria, nuevocollar.estado)
            )
            conn.commit()
            return {"resultado": "Collar registrado exitosamente"}

        except mysql.connector.Error as err:
            conn.rollback()
            return {"error": f"Error en la base de datos: {err}"}

        finally:
            conn.close()

    # CREAR ROL

    def create_rol(self, nuevorol: NuevoRol):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO roles (nombre,estado) VALUES (%s, %s)",
                           (nuevorol.nombre, nuevorol.estado))
            conn.commit()
            conn.close()
            return {"resultado": "Rol creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    # CREAR MODULO

    def create_modulo(self, nuevomodulo: NuevoModulo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO modulos (nombre_modulo,estado) VALUES (%s, %s)",
                           (nuevomodulo.nombre_modulo, nuevomodulo.estado))
            conn.commit()
            conn.close()
            return {"resultado": "Modulo creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
