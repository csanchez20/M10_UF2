#Este archivo contiene el delete, que sirve para eliminar datos de la base de datos que nosotros le digamos

from connection import *

delete = """ DELETE FROM public.cars WHERE car_id=1
    """

print(delete)
connectcion.execute(delete)
print(connectcion)
conn.commit()