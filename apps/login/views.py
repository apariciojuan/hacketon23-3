from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponseForbidden, JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import ensure_csrf_cookie
from django.urls import reverse, reverse_lazy

import json


# Create your views here.
@ensure_csrf_cookie
def login_view(request):
    return render(request, 'login.html')

#@ensure_csrf_cookie
def check_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        datos = open("apps/login/users.json")
        users = datos.read()
        datos.close()
        users = json.loads(users)
        for x in range(len(users)):
            if (username in users[x]['email']) and (password in users[x]['password']):
                return HttpResponseRedirect('/welcome/')
    ctx = {"status": "error", "code": 401, "message": "User or password not found"}
    return JsonResponse(ctx)

def listar_view(request):
    datos = open("products.json")
    produc = datos.read()
    datos.close()
    produc = json.loads(produc)
    if 'filtro' in request.GET:
        if request.GET['filtro'] != '':
            datos2 = {'products': []}
            for x in range(len(produc)):
                if produc['products'][x]['title'] == request.GET['filtro']:
                    datos2['products'].append(produc['products'][x])
            return render(request, 'produc.html', {'datos': datos2})
    return render(request, 'produc.html', {'datos': produc})
