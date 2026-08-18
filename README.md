# Backend SSAH RRHH

Este repositorio contiene la estructura base para una API en Python con enfoque DDD/Clean Architecture.

## Estructura principal

- src/app: módulos de la aplicación
- src/config: configuración global
- migrations: migraciones de base de datos
- tests: pruebas unitarias, de integración y e2e

## Requisitos

- Python 3.11+
- pip o uv

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
pip install -U pip
pip install -e .[dev]
```

## Ejecución

```bash
uvicorn src.app.main:app --reload
```

# http://127.0.0.1:8000/docs

# documentación automática


## Variables de entorno

Copia `.env.example` a `.env` y ajusta los valores.
# BACKEND_SSAH_RRHH
# BACKEND_SSAH_RRHH
# BACKEND_SSAH_RRHH
