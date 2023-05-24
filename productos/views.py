from django.shortcuts import render,get_object_or_404
from .models import Producto,Categoria
# Create your views here.

def list(request):
    productos=Producto.objects.all()
    categorias=Categoria.objects.all()
    return render(request, "index.html", {"productos":productos,"categorias": categorias})

def listDetail(request,pk):
    categorias=Categoria.objects.all()
    producto=get_object_or_404(Producto,pk=pk)
    return render(request, "productDetail.html", {"producto":producto,"categorias": categorias})

def searchProduct(request):
    query =request.GET["producto"].strip()
    categorias=Categoria.objects.all()
    productos = Producto.objects.filter(nombre__icontains=query)
    return render(request, 'index.html', {"productos":productos,"categorias": categorias})



def getByCatgorias(request, category):
    categorias=Categoria.objects.all()
    productos=Producto.objects.filter(categoria__nombre=category)
    return render(request, "index.html",{"productos":productos,"categorias": categorias})


def about(request):
    categorias=Categoria.objects.all()
    return render(request, "About.html",{"categorias": categorias})
def contacto(request):
    categorias=Categoria.objects.all()
    return render(request, "contacto.html",{"categorias": categorias})