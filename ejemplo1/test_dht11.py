import adafruit_dht
import board
import time

SENSOR = adafruit_dht.DHT11(board.D4) #GPIO 4  

try:
    while True:
        try: 
            # Leer los datos
            temperatura = SENSOR.temperature
            humedad = SENSOR.humidity

            # Verificar lectura
            if humedad is not None and temperatura is not None:
                print(f"Temperatura: {temperatura:.1f} C")
                print(f"Humedad: {humedad:.1f}%")
            else:
                print("Error al leer el sensor")
            time.sleep(2)
        except RuntimeError as e:
            print(f"Error de lectura: {e}. Intentando de nuevo...")
except KeyboardInterrupt:
    print("Saliendo...")
finally:
    SENSOR.exit()