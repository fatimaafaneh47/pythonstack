from django.urls import path     
from . import views

app_name='the_wall'

urlpatterns = [
    path('',views.success),
    path('/postmessage',views.message),
    path('/comment/<int:id>',views.comment)
]
