from django.urls import path     
from . import views
urlpatterns = [
    path('',views.main_page),
    path('register',views.registration),
    path('login',views.login),
    path('logout',views.logout),

]
