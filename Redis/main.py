import redis
import time

# Conexión a Redis
client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)


# Función para medir el tiempo de ejecución
def measure_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    elapsed_time = time.time() - start_time
    return result, elapsed_time

# Create (Inserción masiva)
def redis_create():
    data = {f"user:{i}": f"User{i}, {i % 50 + 20}, Address{i}" for i in range(1, 10001)}
    pipe = client.pipeline()
    for key, value in data.items():
        pipe.set(key, value)
    _, elapsed = measure_time(pipe.execute)
    print(f"Redis Create: {elapsed:.2f} seconds")

# Read (Consulta por clave primaria)
def redis_read():
    _, elapsed = measure_time(client.get, "user:5000")
    print(f"Redis Read (Primary Key): {elapsed:.6f} seconds")

# Update (Actualización masiva)
def redis_update():
    keys = client.keys("user:*")
    pipe = client.pipeline()
    for key in keys:
        pipe.set(key, "UpdatedData")
    _, elapsed = measure_time(pipe.execute)
    print(f"Redis Update: {elapsed:.2f} seconds")

# Delete (Eliminación masiva)
def redis_delete():
    keys = client.keys("user:*")
    pipe = client.pipeline()
    for key in keys:
        pipe.delete(key)
    _, elapsed = measure_time(pipe.execute)
    print(f"Redis Delete: {elapsed:.2f} seconds")

# Ejecutar pruebas
if __name__ == "__main__":
    redis_create()
    redis_read()
    redis_update()
    redis_delete()
