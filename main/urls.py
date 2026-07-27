from django.urls import path
from .views import Index,Home
urlpatterns=[
    path('index/',Index),
    path('home/',Home),
    
    


]
