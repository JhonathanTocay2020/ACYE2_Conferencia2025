import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import mysql.connector
from sklearn.neighbors import KNeighborsClassifier

# Configuracion de la base de datos MySQL
DB_CONFIG = {
    'host': '34.145.181.199',  # Servidor MySQL
    'user': 'root',  # Usuario de MySQL
    'password': 'M]Jy9J_/>*ks*C+',  # Contraseña de MySQL
    'database': 'db_conf'  # Nombre de la base de datos
}

# Conexion a la base de datos
conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

# Cargar los datos desde la base de datos
df = pd.read_sql("SELECT id, temperatura FROM dht11_data", conn)

# Cerrar la conexion
cursor.close()
conn.close()

# Definir categorias climaticas y entrenamiento
X_train = np.array([[10], [24], [25], [26], [30], [35]])
y_train = np.array(["Frio", "Frio", "Templado", "Templado", "Caluroso", "Caluroso"])

# Entrenar modelo KNN
model = KNeighborsClassifier(n_neighbors=1)
model.fit(X_train, y_train)

# Clasificar los datos
df["Categoria"] = model.predict(df[["temperatura"]])

# Definir colores personalizados
colores = {"Frio": "blue", "Templado": "green", "Caluroso": "red"}

# Graficar
plt.figure(figsize=(10, 5))
sns.scatterplot(x=df.index, y=df["temperatura"], hue=df["Categoria"], palette=colores, s=100)
plt.xlabel("Tiempo")
plt.ylabel("Temperatura (C)")
plt.title("Clasificacion del Clima")
plt.legend(title="Categoria Climatica")
plt.show()
