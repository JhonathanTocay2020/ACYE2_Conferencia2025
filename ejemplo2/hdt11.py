import mysql.connector
import adafruit_dht
import board
import time

# Configuracion del sensor
SENSOR = adafruit_dht.DHT11(board.D4)

# Configuracion de la base de datos MySQL
DB_CONFIG = {
    'host': '34.145.181.199',  # servidor MySQL
    'user': 'root',             # Usuario de MySQL
    'password': 'M]Jy9J_/>*ks*C+',  # contra de MySQL
    'database': 'db_conf'  # nombre de tu base de datos
}

# Conexion a la base de datos
conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

# Crear tabla para los datos si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS dht11_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    temperatura FLOAT,
    humedad FLOAT
)
''')
conn.commit()  # Aplicar los cambios

try:
    while True:
        try:
            # Leer los datos del sensor
            temperatura = SENSOR.temperature
            humedad = SENSOR.humidity
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")  # Formato de fecha y hora

            # Verificar si la lectura fue exitosa
            if humedad is not None and temperatura is not None:
                print(f"Temperatura: {temperatura:.1f} C")
                print(f"Humedad: {humedad:.1f}%")

                # Guardar los datos en la base de datos
                cursor.execute('''
                    INSERT INTO dht11_data (timestamp, temperatura, humedad)
                    VALUES (%s, %s, %s)
                ''', (timestamp, temperatura, humedad))
                conn.commit()  # Aplicar los cambios
            else:
                print("Error al leer el sensor")
        except RuntimeError as e:
            print(f"Error de lectura: {e}, reintentando en 2 segundos...")
        
        time.sleep(2)  # Esperar 2 segundos entre lecturas

except KeyboardInterrupt:
    print("Programa detenido por el usuario")
finally:
    SENSOR.exit()
    cursor.close()
    conn.close()
