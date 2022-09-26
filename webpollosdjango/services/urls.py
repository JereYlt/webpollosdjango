from django.urls import path
from .import views

urlpatterns = [
    #Paths de service
    
    path('', views.services, name="services"),
   
  
]