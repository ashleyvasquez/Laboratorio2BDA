from pymongo import MongoClient
import time

client = MongoClient('localhost', 27017)
db = client.test_database
collection = db.test_collection

# Función para medir el tiempo de ejecución
def measure_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    elapsed_time = time.time() - start_time
    return result, elapsed_time

# Create (Inserción masiva)
def mongo_create():
    data = [{"id": i, "name": f"User{i}", "age": i % 50 + 20, "address": f"Address{i}"} for i in range(1, 10001)]
    _, elapsed = measure_time(collection.insert_many, data)
    print(f"MongoDB Create: {elapsed:.2f} seconds")

# Read (Consulta por clave primaria)
def mongo_read():
    _, elapsed = measure_time(collection.find_one, {"id": 5000})
    print(f"MongoDB Read (Primary Key): {elapsed:.6f} seconds")

# Update (Actualización masiva)
def mongo_update():
    _, elapsed = measure_time(collection.update_many, {}, {"$set": {"age": 30}})
    print(f"MongoDB Update: {elapsed:.2f} seconds")

# Delete (Eliminación masiva)
def mongo_delete():
    _, elapsed = measure_time(collection.delete_many, {})
    print(f"MongoDB Delete: {elapsed:.2f} seconds")

# Ejecutar pruebas
if __name__ == "__main__":
    mongo_create()
    mongo_read()
    mongo_update()
    mongo_delete()
