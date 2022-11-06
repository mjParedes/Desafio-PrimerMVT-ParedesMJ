from django.http import HttpResponse
from myApp.models import DataFamily
from django.shortcuts import render
# from django.template import Context, Template, loader

# Create your views here.
def mostrarData(request):
    
    datos = DataFamily.objects.all()

    return render(request, "myApp/mainTemplate.html", {"datos":datos})