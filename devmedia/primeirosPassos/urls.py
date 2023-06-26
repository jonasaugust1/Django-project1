from django.urls import path
from django.conf.urls import include
from .views import listar_registros

urlpatterns = [
    path('lista_registros/', listar_registros),
]

# ^ para o inicio do texto
# $ para o final do texto
# \d para um dígito
# + para indicar que o item anterior deve ser repetido pelo menos uma vez
# () para capturar parte do padrão