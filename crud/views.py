from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from .models import Libros, Autor, Biblioteca, CodigoDeBarra
from .forms import LibrosForm
from django.urls import reverse_lazy


# Create your views here.
def create_view (request):
    context = {}

    form = LibrosForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context['form'] = form

    return render(request, "create.html", context)

def list_view (request):
    context = {}
    context['libros'] = Libros.objects.all()


    return render(request, "list.html", context)

def detail_view (request, id):
    context = {}
    context['x'] = Libros.objects.get(id=id)
    context['autores'] = Autor.objects.filter(libros__id=id)
    context['bibliotecas'] = Biblioteca.objects.filter(libros__title__startswith="El")
    context['codigos'] = CodigoDeBarra.objects.filter(libro__id__contains=1)
    print (context['autores'], context['bibliotecas'], context['codigos'])

    return render(request, "detail_view.html", context)

def update_view (request, id):
    context = {}
    obj = get_object_or_404(Libros, id=id)

    form = LibrosForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy('list'))

    context['form'] = form

    return render(request, "update.html", context)

def delete_view (request, id):
    context = {}
    obj = get_object_or_404(Libros, id=id)

    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect(reverse_lazy('list'))

    return render(request, "delete.html", context)