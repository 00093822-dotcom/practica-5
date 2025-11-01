import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='bsjspmx4plunfz2plczz-mysql.services.clever-cloud.com',
            user='uhnwy9ryei16hk86',
            password='zSmgMm8kp5aabLCON5YF',
            database='bsjspmx4plunfz2plczz',
            port=3306
        )
        if conexion.is_connected():
            print("✅ Conexión establecida")
            return conexion
        else:
            print("❌ Conexión fallida (is_connected = False)")
            return None
    except mysql.connector.Error as e:
        print(f"❌ Error al conectar: {e}")
        return None
