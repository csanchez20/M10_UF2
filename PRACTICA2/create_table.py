#Este archivo contiene el create table, que es la creacion de la tabla con el import a la conexion
from connection import *

create_table = """CREATE TABLE CARS(
                      car_id SERIAL PRIMARY KEY,
                      car_model VARCHAR(255) NOT NULL,
                      car_year BIGINT NOT NULL,
                      car_color VARCHAR(255) NOT NULL,
                      car_country VARCHAR(255) NOT NULL,
                      car_type VARCHAR(255) NOT NULL
)"""

print(create_table)
connectcion.execute(create_table)
print(connectcion)
conn.commit()