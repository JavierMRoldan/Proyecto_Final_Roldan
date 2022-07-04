from xml.etree.ElementInclude import include
from django.urls import path , include, re_path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns =  [

    path("", views.blogs , name='blogs'),
    path('alta_blog', views.blog_formularios, name='alta_blog'),
    path('eliminar_blog/<int:id>', views.eliminar_blog, name="eliminar_blog"),
    path("editar_blog/<int:id>", views.editar_blog , name="editar_blog"),
    path("editar_blog/", views.editar_blog , name="editar_blog"),
    
    path("<int:id>", views.pagesid , name="pagesid"),
    # re_path(r'(?P<ip>\d+)/$', views.pagesid)


]