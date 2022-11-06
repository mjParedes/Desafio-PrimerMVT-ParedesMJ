from django.http import HttpResponse
from django.template import Template, Context 


def saludo(request):
    return HttpResponse("""
    <h1>Welcome to Cinemafy</h1>
    <h3>Hogar del septimo arte</h3>
    """)

def plantillaInicio(request):
    archivo = open(r"C:\Users\Usuario\Documents\Desafios-Python_CoderHouse\Desafio-NuestroPrimerMVT\primermvt\primermvt\templates\plantilla_inicio.html")

    plantilla = Template(archivo.read())

    archivo.close()

    contexto = Context()

    documento = plantilla.render(contexto)

    return HttpResponse(documento)

