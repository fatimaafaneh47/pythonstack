from django.urls import path     
from . import views
urlpatterns = [
    path('shows',views.all_shows),
    path('shows/new',views.new_show),
    path('shows/create',views.add_show),
    path('shows/<int:show_id>',views.tv_show),
    path('shows/<int:show_id>/delete',views.delete),
    path('shows/<int:show_id>/edit',views.edit_page),
    path('shows/<int:show_id>/update',views.update)
    
]