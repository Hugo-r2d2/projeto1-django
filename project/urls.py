from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse('HOME')

def contato(request):
    return HttpResponse('CONTATO')

def sobre(request):
    return HttpResponse('SOBRE')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
]

