from connection import *

insert = """ INSERT INTO public.cars (car_id, car_model, car_year, car_color, car_country, car_type)
                        VALUES ('1', 'Ferrari', 2000, 'Rojo', 'Italia', 'Deportivo')

"""

print(insert)
connectcion.execute(insert)
print(connectcion)
conn.commit()