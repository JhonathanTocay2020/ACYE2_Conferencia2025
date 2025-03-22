## Instalar Mysql

```bash
pip install mysql-connector-python
```

otorgar Permisos de Usuario a la Raspberry

```bash
GRANT ALL PRIVILEGES ON tu_base_de_datos.* TO 'tu_usuario'@'%' IDENTIFIED BY 'tu_contraseña';

FLUSH PRIVILEGES;
```
- Ejemplo 
```bash
GRANT ALL PRIVILEGES ON data_arqui1.* TO 'root'@'192.168.1.12' IDENTIFIED BY 'mysql1234';
FLUSH PRIVILEGES;
```