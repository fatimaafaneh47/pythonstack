#from crypt import methods
from django.urls import path
from . import views	
                    
urlpatterns = [
    path('', views.root),
    path('result',views.display),
    
]