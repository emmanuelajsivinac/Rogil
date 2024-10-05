import redis


client = redis.StrictRedis(host='192.168.0.8', port=6379, db=0)


try:
    client.ping()
    print("Conectado a Redis")
except redis.ConnectionError:
    print("No se pudo conectar a Redis")
