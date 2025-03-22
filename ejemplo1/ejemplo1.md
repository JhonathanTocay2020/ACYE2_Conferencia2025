
# Ejemplo 1 - Encender una led

```PYTHON
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

while True:
  GPIO.output(7, True)
  time.sleep(1)
  GPIO.output(7, False)
  time.sleep(1)
```

# DHT11 - Encender una led

## Crear Entorno Virtual

### 1. Crear un Entorno Virtual 

Instalar los paquetes en un entorno virtual 

1. Instalar las herramientas necesarias: Asegúrate de tener instalado python3-venv:
```bash
sudo apt install python3-venv
```

2. Crear un entorno virtual:
```bash
python3 -m venv ~/dht11
```

3. Activar el entorno virtual:
```bash
source ~/dht11/bin/activate
```

4. Instalar adafruit-circuitpython-dht dentro del entorno: 
- Consideraciones: Instalar cuando este activado el entorno.
- Instala el paquete:

```bash
pip install adafruit-circuitpython-dht
sudo apt install libgpiod2
```
