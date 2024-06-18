from django.urls import path
from . import views

urlpatterns = [
    path('servicios/', views.listar_servicios, name='listar_servicios'),
]