# Fast API Project

Este proyecto es una aplicación web construida con FastAPI, diseñada para manejar operaciones CRUD para ítems. A continuación se presenta una descripción de la estructura del proyecto y sus componentes principales.

## Estructura del Proyecto

```
fast-api-project
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── dependencies.py
│   │   └── routes
│   │       ├── __init__.py
│   │       └── v1
│   │           ├── __init__.py
│   │           └── endpoints
│   │               ├── __init__.py
│   │               └── items.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── security.py
│   ├── db
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── session.py
│   ├── models
│   │   ├── __init__.py
│   │   └── item.py
│   └── schemas
│       ├── __init__.py
│       └── item.py
├── tests
│   ├── __init__.py
│   ├── conftest.py
│   └── test_api
│       ├── __init__.py
│       └── test_items.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Instalación

1. Clona el repositorio:
   ```
   git clone <URL_DEL_REPOSITORIO>
   cd fast-api-project
   ```

2. Crea un entorno virtual y actívalo:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Uso

Para ejecutar la aplicación, utiliza el siguiente comando:
```
uvicorn app.main:app --reload
```

Esto iniciará el servidor en `http://127.0.0.1:8000`.

## Pruebas

Las pruebas se encuentran en el directorio `tests`. Para ejecutar las pruebas, utiliza:
```
pytest
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.