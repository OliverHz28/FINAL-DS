# Imagen base de Python
FROM python:3.9-slim

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos los archivos del microservicio
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Este comando inicia el servidor FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]