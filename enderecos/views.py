from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Endereco


def home(request):
    data = {'now': datetime.datetime.now(), 'enderecos': Endereco.objects.all()}
    # html = '<html><body>Olá! Hoje é %s.</body></html>' % now
    return render(request, 'enderecos/home.html', data)
