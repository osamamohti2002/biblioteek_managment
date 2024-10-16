from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('update', views.update, name='update'),
    path('delete', views.delete, name='delete'),
    path('books', views.books, name='books'),
]