#Este archivo contiene el update, que sirve para actualizar datos de la base de datos que nosotros le digamos

from connection import *

update = """ UPDATE public.cars SET car_country='Italia' WHERE car_id=1
   """

connectcion.execute(update)
conn.commit()
result = connectcion.rowcount

print("id modificada: ", result, "Actualització efectuada correctament.")