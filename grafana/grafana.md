# Instalar Grafana

```bash
sudo apt install -y software-properties-common
sudo add-apt-repository "deb https://apt.grafana.com stable main"
sudo apt update
sudo apt install -y grafana
```

#### Activa y arranca Grafana:

```bash
sudo systemctl enable grafana-server
sudo systemctl start grafana-server
```

Accede a Grafana desde tu navegador en http://<IP_RASPBERRY>:3000 (usuario: admin, contraseña: admin).

## Solución: Agregar la clave GPG de Grafana manualmente

```bash
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://apt.grafana.com/gpg.key | sudo tee /etc/apt/keyrings/grafana.asc > /dev/null
```

agrega el repositorio de Grafana correctamente:

```bash
echo "deb [signed-by=/etc/apt/keyrings/grafana.asc] https://apt.grafana.com stable main" | sudo tee /etc/apt/sources.list.d/grafana.list
```

Ahora instala Grafana sin problemas:

```bash
sudo apt install grafana -y
```

Una vez instalado, inicia el servicio:

```bash
sudo systemctl enable grafana-server
sudo systemctl start grafana-server
```

Verifica que esté funcionando:

```bash
sudo systemctl status grafana-server
```
