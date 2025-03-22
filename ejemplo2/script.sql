-- create database db_conf;
use db_conf;

CREATE TABLE IF NOT EXISTS dht11_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    temperatura FLOAT,
    humedad FLOAT
);

select * from dht11_data;