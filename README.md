#Bases de Datos Avanzadas
# Laboratorio2 

# Configuración de Redis, MongoDB y Entorno Virtual en Python para Pruebas de Rendimiento

Este documento describe los pasos para configurar Redis, MongoDB y un entorno virtual en Python en un Mac M1.

## Requisitos previos
- **Homebrew** instalado en tu sistema. Si no lo tienes, instala Homebrew ejecutando:
  ```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```

---

## Instalación y Configuración de Redis

1. **Instalar Redis:**
   ```bash
   brew install redis
   ```

2. **Iniciar Redis:**
   ```bash
   brew services start redis
   ```

3. **Verificar que Redis está funcionando:**
   ```bash
   redis-cli ping
   ```
   Deberías obtener como respuesta `PONG`.

---

## Instalación y Configuración de MongoDB

1. **Agregar el repositorio de MongoDB a Homebrew:**
   ```bash
   brew tap mongodb/brew
   ```

2. **Instalar MongoDB:**
   ```bash
   brew install mongodb-community@6.0
   ```

3. **Iniciar MongoDB:**
   ```bash
   brew services start mongodb/brew/mongodb-community@6.0
   ```

4. **Verificar que MongoDB está funcionando:**
   ```bash
   mongo --eval "db.runCommand({ connectionStatus: 1 })"
   ```
   Deberías obtener una respuesta JSON indicando que la conexión está activa (campo `ok` igual a 1).

---

## Configuración del Entorno Virtual en Python

1. **Crear un entorno virtual:**
   ```bash
   python3 -m venv env
   ```

2. **Activar el entorno virtual:**
   ```bash
   source env/bin/activate
   ```

3. **Instalar las dependencias necesarias:**
   ```bash
   pip install redis pymongo
   ```

4. **Probar la conexión a Redis:**
   Crea un archivo `test_redis.py` con el siguiente contenido:
   ```python
   import redis

   r = redis.Redis(host='localhost', port=6379, decode_responses=True)
   r.set('key', 'value')
   print(r.get('key'))
   ```
   Ejecuta el script:
   ```bash
   python test_redis.py
   ```

5. **Probar la conexión a MongoDB:**
   Crea un archivo `test_mongo.py` con el siguiente contenido:
   ```python
   from pymongo import MongoClient

   client = MongoClient('localhost', 27017)
   db = client.test_database
   collection = db.test_collection
   collection.insert_one({"name": "test"})
   print(list(collection.find()))
   ```
   Ejecuta el script:
   ```bash
   python test_mongo.py
   ```

---

Con esto, tienes configurados Redis, MongoDB y un entorno virtual en Python listos para realizar pruebas de rendimiento.
