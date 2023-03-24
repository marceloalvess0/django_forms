from django.urls import path
from . import views

urlpatterns = [
    path('',views.passagens, name='passagens'),
    path('minha_consulta',views.revisao_consulta, name='minha_consulta')
]
