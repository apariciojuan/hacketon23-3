from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
import datetime

def index_view(request):
    return render(request, 'index.html', {'hola': 'Hello world!'})

def health_check_view(request):
    return render(request, 'date.html', {'value': datetime.datetime.now()})
