import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.collares_gps_model import Collares_GPS
from fastapi.encoders import jsonable_encoder


class CollarGPScontroller():

    # CREAR COLLARGPS
    def create_collar_gps(self, collares_gps: Collares_GPS):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO collares_con_gps (numero_serie,ultima_ubicacion_registrada,nivel_bateria,id_mascota_vinculada,estado) VALUES (%s, %s, %s, %s, %s)",
                           (collares_gps.numero_serie, collares_gps.ultima_ubicacion_registrada, collares_gps.nivel_bateria, collares_gps.fecha_hora_ultimo_reporte, collares_gps.id_mascota_vinculada, collares_gps.estado))
            conn.commit()
            conn.close()
            return {"resultado": "Collar Registrado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    # BUSCAR COLLARGPS
    def get_collargps(self, collargps_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM collares_con_gps WHERE id = %s", (collargps_id,))
            result = cursor.fetchone()
            payload = []
            content = {}

            content = {
                "id": int(result[0]),
                "numero_serie": result[1],
                "ultima_ubicacion_registrada": result[2],
                "nivel_bateria": int(result[3]),
                "fecha_hora_ultimo_reporte": result[4],
                "id_mascota_vinculada": int(result[5]),
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

    # VER COLLARESGPS
    def get_collaresgps(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM collares_con_gps")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    'id': int(data[0]),
                    'numero_serie': data[1],
                    'ultima_ubicacion_registrada': data[2],
                    'nivel_bateria': int(data[3]),
                    'fecha_hora_ultimo_reporte': data[4],
                    'id_mascota_vinculada': int(data[5]),
                    'estado': bool(data[6]),
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="Collares not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    # ACTUALIZAR COLLARGPS
    def update_collargps(self, collargps_id: int, collares_gps: Collares_GPS):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE collares_con_gps SET numero_serie = %s, ultima_ubicacion_registrada = %s, nivel_bateria=%s,fecha_hora_ultimo_reporte=%s, id_mascota_vinculada=%s, estado = %s WHERE id = %s",
                           (collares_gps.numero_serie, collares_gps.ultima_ubicacion_registrada, collares_gps.nivel_bateria, collares_gps.fecha_hora_ultimo_reporte, collares_gps.id_mascota_vinculada, collares_gps.estado, collargps_id))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(
                    status_code=404, detail="Collar not found")
            return {"mensaje": "Datos de CollarGPS actualizado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    # ELIMINAR COLLARGPS
    def delete_collargps(self, collargps_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM collares_con_gps WHERE id = %s",
                           (collargps_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(
                    status_code=404, detail="CollarGPS no encontrado")
            return {"mensaje": "CollarGPS eliminado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    # FIN COLLARGPS
