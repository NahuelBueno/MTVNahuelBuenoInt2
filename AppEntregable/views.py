from django.shortcuts import render
from django.http import HttpResponse
from AppEntregable.models import Familia
from django.template import loader

def familia(self):
    familia1 = Familia(nombre = "Christian", edad = 26, fecha_nac = "1996-1-12")
    familia1.save()

    familia2 = Familia(nombre = "Christopher", edad = 26, fecha_nac = "1996-1-12")
    familia2.save()

    familia3 = Familia(nombre = "Janis", edad = 32, fecha_nac = "1991-5-31")
    familia3.save()

    diccionario = {
        "nome1": familia1.nombre, "edade1": familia1.edad, "nacimento1": familia1.fecha_nac,
        "nome2": familia2.nombre, "edade2": familia2.edad, "nacimento2": familia2.fecha_nac,
        "nome3": familia3.nombre, "edade3": familia3.edad, "nacimento3": familia3.fecha_nac
        }
    
    mensaje = Familia.objects.all()
    print(mensaje)
    
    plantilla = loader.get_template("familiar.html")
    document = plantilla.render(diccionario)

    return HttpResponse(document)