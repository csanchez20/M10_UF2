#Este archivo contiene el read, que sirve para leer datos de la base de datos que nosotros le digamos
from connection import *

leer = """ SELECT car_id, car_model, car_year, car_color, car_country, car_type
                    FROM public.cars
    """

connectcion.execute(leer)

result = connectcion.fetchall()

for i in result:
    print("car_id: ", i[0],)
    print("car_model: ", i[1],)
    print("car_year: ", i[2],)
    print("car_color: ", i[3],)
    print("car_country: ", i[4],)
    print("car_type: ", i[5], "\n")