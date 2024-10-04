import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.atributoxusuario_model import AtributoxUsuario
from fastapi.encoders import jsonable_encoder


class AtributoxUsuariocontroller():

    # CREAR ATRIBUTOXUSUARIO
    def create_atributoxusuario(self, atributoxusuario: AtributoxUsuario):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO atributoxusuario (id_usuario, id_atributo, valor, descripcion, estado) VALUES (%s,%s,%s,%s,%s)",
                           (atributoxusuario.id_usuario, atributoxusuario.id_atributo, atributoxusuario.valor, atributoxusuario.descripcion, atributoxusuario.estado))
            conn.commit()
            conn.close()
            return {"resultado": "Atributoxusuario creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    # BUSCAR ATRIBUTOXUSUARIO
    def get_atributoxusuario(self, atributoxusuario_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM atributoxusuario WHERE id = %s", (atributoxusuario_id,))
            result = cursor.fetchone()
            payload = []
            content = {}

            content = {
                'id': int(result[0]),
                'id_usuario': int(result[1]),
                'id_atributo': int(result[2]),
                'valor': (result[3]),
                'descripcion': (result[4]),
                'estado': bool(result[5]),
            }
            payload.append(content)

            json_data = jsonable_encoder(content)
            if result:
                return json_data
            else:
                raise HTTPException(
                    status_code=404, detail="Atributoxusuario not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    # VER atributoxusuario
    def get_atributoxusuarios(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM atributoxusuario")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    'id': int(data[0]),
                    'id_usuario': int(data[1]),
                    'id_atributo': int(data[2]),
                    'valor': data[3],
                    'descripcion': data[4],
                    'estado': bool(data[5]),
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="Atributosxusuario not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    # ACTUALIZAR ATRIBUTOXUSUARIO
    def update_atributoxusuario(self, atributoxusuario_id: int, atributoxusuario: AtributoxUsuario):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE atributoxusuario SET id_usuario	= %s, id_atributo = %s, valor = %s, descripcion = %s, estado = %s WHERE id = %s",
                (atributoxusuario.id_usuario, atributoxusuario.id_atributo,
                 atributoxusuario.valor, atributoxusuario.descripcion, atributoxusuario.estado, atributoxusuario_id,)
            )
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(
                    status_code=404, detail="AtributoxUsuario no encontrado")

            return {"mensaje": "AtributoxUsuario actualizado exitosamente"}

        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))

        finally:
            if conn:
                conn.close()

    # ELIMINAR ATRIBUTOXUSUARIO
    def delete_atributoxusuario(self, atributoxusuario_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM atributoxusuario WHERE id = %s", (atributoxusuario_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(
                    status_code=404, detail="AtributoxUsuario no encontrado")
            return {"mensaje": "AtributoxUsuario eliminado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()
