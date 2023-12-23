from . import views
from .views import BookView, home
from django.urls import path

app_name = 'book_rating'

urlpatterns = [
    path('', home, name="home"),
    path('books', BookView.as_view(), name="books"),
    path('search', views.search, name="search"),
    path('like', views.like, name="like_book")
]