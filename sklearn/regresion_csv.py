import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Cargar los datos
df = pd.read_csv("datos.csv")

# Convertir a valores numericos y manejar NaN
df["Temperatura"] = pd.to_numeric(df["Temperatura"], errors="coerce")
df["Humedad"] = pd.to_numeric(df["Humedad"], errors="coerce")
df = df.dropna()  # Eliminar filas con valores NaN

# Separar variables
X = df[["Temperatura"]]  # Variable independiente
y = df["Humedad"]        # Variable dependiente

# Dividir en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresion lineal
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Prediccion
y_pred = modelo.predict(X_test)

# Evaluacion del modelo
print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f}")
print(f"R2: {r2_score(y_test, y_pred):.2f}")

# Visualizacion
plt.scatter(X_test, y_test, color="blue", label="Datos reales", alpha=0.6)
plt.plot(X_test, y_pred, color="red", linewidth=2, label="Regresion Lineal")
plt.xlabel("Temperatura")
plt.ylabel("Humedad")
plt.title("Regresion Lineal: Temperatura vs Humedad")
plt.legend()
plt.grid(True)
plt.show()