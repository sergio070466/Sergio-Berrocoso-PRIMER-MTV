from django.urls import path, include
from miappfamilia.views import *

urlpatterns = [
    path('familia/', familia),
    path('pantalones/', pantalones),
    path('camisas/', camisas),
      
]   

