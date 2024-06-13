from django.shortcuts import render, redirect

from inicio.models import Bici
from inicio.forms import CrearBiciFormulario, BuscarBici, EditarBiciFormulario

import random

def inicio(request):
    return render(request, 'inicio/index.html')

def probando(request):
    
    lista = list(range(500))
    
    numeros = random.choices(lista, k=50)
    print(numeros)
    return render(request, 'probando_if_for.html', {'numeros': numeros})

def crear_bici(request, marca, modelo):
    bici = Bici(marca=marca, modelo=modelo)
    bici.save()
    return render(request, 'bici_templates/creacion.html', {"bici": bici})

def crear_bici_v2(request):
    print('Valor de la request: ', request)
    print('Valor de GET: ', request.GET)
    print('Valor de POST: ', request.POST)
    
    formulario = CrearBiciFormulario()
    
    if request.method == 'POST':
        formulario = CrearBiciFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            bici = Bici(marca=datos.get('marca'), modelo=datos.get('modelo'))
            bici.save()
            return redirect('bicis')

    return render(request, 'inicio/crear_bici_v2.html', {'formulario': formulario})

def autos(request):
    
    formulario = BuscarBici(request.GET)
    if formulario.is_valid():
        marca = formulario.cleaned_data['marca']
        bicis = Bici.objects.filter(marca__icontains=marca)
    
    return render(request, 'inicio/bicis.html', {'bicis': bicis, 'formulario': formulario})
    
def eliminar_bici(request, id):
    bici = Bici.objects.get(id=id)
    bici.delete()
    return redirect('autos')
    
def editar_bici(request, id):
    bici = Bici.objects.get(id=id)
    
    formulario = EditarBiciFormulario(initial={'marca': bici.marca, 'modelo': bici.modelo, 'anio': bici.anio})
    
    if request.method == 'POST':
        formulario = EditarBiciFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            
            bici.marca = info['marca']
            bici.modelo = info['modelo']
            bici.anio = info['anio']
            bici.save()
            return redirect('autos')
    
    return render(request, 'inicio/editar_bici.html', {'formulario': formulario, 'auto': bici})
    
def ver_bici(request, id):
    bici = Bici.objects.get(id=id)
    return render(request, 'inicio/ver_bici.html', {'bici': bici})