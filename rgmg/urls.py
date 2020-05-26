
from django.urls import path
from rgmg.views import inicio, tablas, grafico, modelo, analisis, histograma

urlpatterns = [
    path('', inicio),
    path('index.html', inicio),
    path('tables.html', tablas),  
    path('charts.html', grafico),
    path('buttons.html', modelo),
    path('form-elements.html', analisis),
    path('typography.html', histograma),
           
]
