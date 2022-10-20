from django.urls import path     
from . import views

app_name='book'

urlpatterns = [
    path('',views.success),
    path('/add_books/',views.add),
    path('/<int:book_id>',views.single_book),
    path("show/<int:book_id>",views.show),
    path('show_user/<int:book_id>',views.show_user),
    path('/<int:book_id>/update',views.update),
    path('/<int:book_id>/delete',views.delete),
    path('fav/<int:book_id>',views.favorites),
    path('/<int:book_id>/add_fav',views.add_favorites),
    path('/<int:book_id>/delete_fav',views.delete_favorites),

]
