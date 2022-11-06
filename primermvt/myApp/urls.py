from django.urls import path
from myApp.views import *

urlpatterns = [
    path('', mostrarData),
]