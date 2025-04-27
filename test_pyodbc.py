import pyodbc

def test_pyodbc_connection():
    try:
        connection = pyodbc.connect(
            "DRIVER={ODBC Driver 18 for SQL Server};"
            "SERVER=iush-proyecto-aula.database.windows.net,1433;"
            "DATABASE=omega-ubuntu;"
            "UID=admin-aula;"
            "PWD=Sistemas$1234;"
            "Encrypt=yes;"
            "TrustServerCertificate=no;"
            "Connection Timeout=30;"
        )
        print("Conexión exitosa con pyodbc")
        connection.close()
    except Exception as e:
        print("Error al conectar con pyodbc:", e)

if __name__ == "__main__":
    test_pyodbc_connection()