# Imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiamos los archivos del microservicio
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponer el puerto
EXPOSE 5001

# Este comando inicia el servidor FastAPI
CMD ["uvicorn", "service:app", "--host", "0.0.0.0", "--port", "5001"]
