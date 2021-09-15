from config.wsgi import *
from core.erp.models import Type, Employee

# Listar

# select * from tabla
#query = Type.objects.all()
#print(query)

# Inseción
#t = Type()
#t.name = 'hola'
#t.save()

# Edición
#try:
#    t = Type.objects.get(pk=1)
#    t.name = 'Presidente'
#    t.save()
#except Exception as e:
#    print(e)

# Eliminación
#t = Type.objects.get(pk=1)
#t.delete()


#Para consultas a la BD
#obj = Type.objects.filter(name__icontains='terry')

obj = Employee.objects.Filter()

for i in Type.objects.filter():
    print(obj)
