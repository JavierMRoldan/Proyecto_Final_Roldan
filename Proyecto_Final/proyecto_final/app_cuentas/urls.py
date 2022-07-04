from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns =  [

    path("register/", views.register, name="register"),
    path('login/', views.login_request, name = 'login'),
    path("logout/", LogoutView.as_view(template_name='logout.html'), name="logout"),
    path("editar_perfil" , views.editar_perfil, name="editar_perfil"),
    path("inicio", views.inicio, name="inicio"),

]