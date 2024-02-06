# Intenta importar las funciones CRUD y de conexión
try:
    from create import insert
    from read import leer
    from update import update
    from delete import delete
    from connection import conn
except ImportError as e:
    print("Error al importar las funciones:", e)
    exit(1)

def main():
    # Intenta establecer una conexión a la base de datos
    try:
        connectcion = conn()
    except Exception as e:
        print("Error al establecer la conexión:", e)
        exit(1)

    # Ejemplo de uso de las funciones
    try:
        insert(connectcion, "Toyota", 2020, "Rojo", "Japón", "SUV")
        leer(connectcion)
        update(connectcion, 1, "Toyota Camry", 2021, "Azul", "Japón", "Sedán")
        leer(connectcion)
        delete(connectcion, 1)
        leer(connectcion)
    except Exception as e:
        print("Error al ejecutar las operaciones CRUD:", e)
        exit(1)

    # Cierra la conexión a la base de datos
    try:
        connectcion.close()
    except Exception as e:
        print("Error al cerrar la conexión:", e)

    if __name__ == "__main__":
        main()


