from django.urls import path

from blog.views import MovieCreate, AnimeCreate, SoftwareCreate, BookCreate
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.MovieListView.as_view(), name='Movies'),
    path('anime/', views.AnimeListView.as_view(), name='Anime'),
    path('books/', views.BookListView.as_view(), name='Books'),
    path('software/', views.SoftwareListView.as_view(), name='Software'),
    path('movies/<int:pk>', views.MovieDetailView.as_view(), name='Movies-detail'),
    path('anime/<int:pk>', views.AnimeDetailView.as_view(), name='Anime-detail'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='Books-detail'),
    path('software/<int:pk>', views.SoftwareDetailView.as_view(), name='Software-detail'),
    path('register/', views.register, name='register'),
    path('users/', views.user_list, name='user_list'),
    path('users/follow/<username>', views.follow, name='follow_user'),
    path('users/<username>/', views.user_detail, name='user_detail'),
    path('movies/create', MovieCreate.as_view(), name='create_movie'),
    path('anime/create', AnimeCreate.as_view(), name='create_anime'),
    path('software/create', SoftwareCreate.as_view(), name='create_software'),
    path('books/create', BookCreate.as_view(), name='create_book'),
    path('users/update_profile', views.UpdateProfile, name='update_profile'),
]
