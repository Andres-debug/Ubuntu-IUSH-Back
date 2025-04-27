from sqlalchemy.sql import text
from app.db.session import engine

def test_connection():
    try:
        with engine.connect() as connection:
            # Usa text() para ejecutar la consulta
            result = connection.execute(text("SELECT 1"))
            print("Conexión exitosa:", result.fetchone())
    except Exception as e:
        print("Error al conectar a la base de datos:", e)

if __name__ == "__main__":
    test_connection()