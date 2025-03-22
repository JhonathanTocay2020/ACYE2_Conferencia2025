import adafruit_dht
import board
import time
import numpy as np
from sklearn.linear_model import LinearRegression

# Configurar sensor DHT11 en GPIO 4
SENSOR = adafruit_dht.DHT11(board.D4)

# Lista para almacenar datos de temperatura
data_temperaturas = []

try:
    while True:
        try:
            # Leer los datos del sensor
            temperatura = SENSOR.temperature
            humedad = SENSOR.humidity

            # Verificar lectura valida
            if temperatura is not None and humedad is not None:
                print(f"Temperatura actual: {temperatura:.1f} C | Humedad: {humedad:.1f}%")
                
                # Agregar temperatura a la lista
                data_temperaturas.append(temperatura)

                # Asegurar que hay suficientes datos para entrenar (minimo 5)
                if len(data_temperaturas) >= 5:
                    # Preparar datos para el modelo
                    X = np.array(range(len(data_temperaturas))).reshape(-1, 1)
                    y = np.array(data_temperaturas).reshape(-1, 1)

                    # Entrenar modelo de regresion
                    model = LinearRegression()
                    model.fit(X, y)

                    # Predecir temperatura futura
                    next_time = np.array([[len(data_temperaturas)]])  # Siguiente punto en el tiempo
                    temp_predicha = model.predict(next_time)[0][0]

                    print(f"?? Prediccion de temperatura en 2s: {temp_predicha:.1f} C")

            else:
                print("?? Error al leer el sensor, intentando de nuevo...")
            
            time.sleep(2)  # Esperar 2 segundos entre lecturas
        
        except RuntimeError as e:
            print(f"?? Error de lectura: {e}. Reintentando...")

except KeyboardInterrupt:
    print("?? Programa detenido por el usuario")

finally:
    SENSOR.exit()
