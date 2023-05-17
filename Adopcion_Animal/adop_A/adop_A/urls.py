
from django.contrib import admin
from django.urls import path
from .views import mostrar_principal


urlpatterns = [
    path('', mostrar_principal, name= 'pagina_principal'),
    path('admin/', admin.site.urls),
]
