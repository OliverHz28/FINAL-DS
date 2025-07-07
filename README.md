# Examen Final

### Estructura del proyecto:

```
FINAL-DS/
├── docker-compose.yml                 
├── legacy_app/       
│   ├── Dockerfile
│   ├── requirements.txt
│   └── main.py                        
├── new-microservice/       
│   ├── Dockerfile
│   ├── requirements.txt
│   └── service.py      
├── app.db
├── .gitignore
└── README.md        
```

### Configuración Inicial

1. **Clonar el repositorio**
    ```bash
    git clone https://github.com/edysaul20000/PC4-Proyecto-14.git
    cd FINAL-DS/
    ```

2. **Crear y activar el entorno virtual**
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. **Instalar dependencias**
    ```bash
    pip install -r legacy_app/requirements.txt 
    pip install -r  new_microservice/requirements.txt 
    ```

### Ejecutar usando uvicorn individualmente

**Terminal 1 - Service:**
```bash
uvicorn new_microservice.service:app --host 0.0.0.0 --port 8001 --reload
```
**Terminal 2 - app:**
```bash
uvicorn legacy_app.main:app --host 0.0.0.0 --port 8000 --reload
```

**O directamente con Docker Compose:**
```bash
# Iniciar servicios
docker compose up --build

# Detener servicios
docker compose down
```