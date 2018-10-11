from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('editar-perfil/<int:id>', views.editar, name="editar-perfil"),
    path('salvar-perfil/<int:id>', views.salvar, name="salvar"),
]
