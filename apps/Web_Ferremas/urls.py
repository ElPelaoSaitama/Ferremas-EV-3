from django.urls import path
from apps.Web_Ferremas.views import home


urlpatterns = [
    path('',home,name="home")
    
]