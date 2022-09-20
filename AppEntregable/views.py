from django.shortcuts import render
from django.http import HttpResponse
from AppEntregable.models import Familia
from django.template import loader

def familia(self):
    familia1 = Familia(nombre="Gabriela", edad=52, fecha_nac="1975-03-25")
    familia1.save()

    familia2= Familia(nombre="Daniel", edad=55, fecha_nac="1973-02-17")
    familia2.save()

    familia3 = Familia(nombre="Facundo", edad=20, fecha_nac="2001-08-24")
    familia3.save()


    diccionario = {
        "nome1": familia1.nombre, "edade1": familia1.edad, "nacimento1": familia1.fecha_nac,
        "nome2": familia2.nombre, "edade2": familia2.edad, "nacimento2": familia2.fecha_nac,
        "nome3": familia3.nombre, "edade3": familia3.edad, "nacimento3": familia3.fecha_nac
        }
    
    mensaje = Familia.objects.all()
    print(mensaje)
    
    plantilla = loader.get_template("plantilla1.html")
    document = plantilla.render(diccionario)

    return HttpResponse(document)