from django.urls import path
from .views import index,listado,nueva,editar,contacto,lista_personas

urlpatterns = [
    path('', index, name='index'),
    path('listado/', listado, name='listado'),
    path('nueva/', nueva, name='nueva'),
    path('editar/<int:id>', editar, name='editar'),
    path('contacto/', contacto, name='contacto'),   
    path('lista_personas/', lista_personas, name='lista_personas'),

]
