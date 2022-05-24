from django.urls import path #path me permite armar la config de URLS

from . import views  #importo las views

urlpatterns = [
    
    path("cursos/" , views.cursos),
    path("alta_curso/<nombre>" , views.alta_curso)


]