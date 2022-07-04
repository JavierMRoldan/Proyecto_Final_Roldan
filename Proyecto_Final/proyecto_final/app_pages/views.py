from contextlib import ContextDecorator
from email import message
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from app_pages.models import Blogs 
from app_pages.forms import Blog_formulario


# Create your views here.


def blogs(request):
    blogs = Blogs.objects.all()
    dicc = {'blogs' : blogs}
    plantilla = loader.get_template('blogs.html')
    documento = plantilla.render(dicc)
    return HttpResponse( documento )

#----------------------------------------------
@login_required
def blog_formularios(request):

    if request.method == "POST":
        
        mi_blog = Blog_formulario(request.POST)

        if mi_blog.is_valid():
            datos_blog = mi_blog.cleaned_data
            blog = Blogs(titulo=datos_blog['titulo'],subtitulo=datos_blog['subtitulo'],cuerpo=datos_blog['cuerpo'],autor=datos_blog['autor'],fecha=datos_blog['fecha'])
            blog.save()
            return render(request, 'inicio.html')
    
    return render(request, "alta_blog.html")

#----------------------------------------------
@login_required
def eliminar_blog(request, id):
    blog = Blogs.objects.get(id=id)
    blog.delete()

    blog = Blogs.objects.all()

    contexto = {"blogs" : blog}

    return render(request, "blogs.html", contexto)

#----------------------------------------------
@login_required
def editar_blog(request, id):
    
    blog = Blogs.objects.get(id=id)
    
    if request.method == "POST":

        mi_formulario = Blog_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            blog.titulo = datos['titulo']
            blog.subtitulo = datos['subtitulo']
            blog.cuerpo = datos['cuerpo']
            blog.autor = datos['autor']
            blog.fecha = datos['fecha']
            blog.save()

            return redirect(to='blogs')
    else:
        mi_formulario = Blog_formulario(initial={'titulo':blog.titulo , 'subtitulo':blog.subtitulo , 'cuerpo':blog.cuerpo , 'autor':blog.autor , 'fecha':blog.fecha})

    return render(request , "editar_blog.html" , {"mi_formulario":mi_formulario , "blog":blog})

def pagesid(request, id=None):
    blog = None
    if id is not None:
        blog = Blogs.objects.get(id=id)
    context = {
        'blog':blog
    }
    return render(request, 'pages_detail.html', context)
