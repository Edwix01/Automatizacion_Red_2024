from influxdb import InfluxDBClient

# Conexión al servidor InfluxDB
client = InfluxDBClient(host='localhost', port=8086, username='admin', password='admin', database='influx')

# Datos que quieres escribir
data = [
    {
        "measurement": "temperatura",
        "tags": {
            "ubicacion": "sala"
        },
        "fields": {
            "valor": 25.6
        }
    },
    {
        "measurement": "humedad",
        "tags": {
            "ubicacion": "sala"
        },
        "fields": {
            "valor": 60.3
        }
    }
]

# Escribir los datos en InfluxDB
client.write_points(data)

# Cerrar la conexión
client.close()

