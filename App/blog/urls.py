from blog.views import MovieCreate, AnimeCreate, SoftwareCreate, BookCreate, MovieReplyToCommentView
from django.urls import path

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
    path('users/generateuserdata', views.generate_user_data, name='generate_user_data'),
    path('users/follow/<username>', views.follow, name='follow_user'),
    path('users/<username>/', views.user_detail, name='user_detail'),
    path('movies/create', MovieCreate.as_view(), name='create_movie'),
    path('movies/reply_to_comment/<int:pk>', MovieReplyToCommentView.as_view(), name='reply_to_comment'),
    path('anime/create', AnimeCreate.as_view(), name='create_anime'),
    path('software/create', SoftwareCreate.as_view(), name='create_software'),
    path('books/create', BookCreate.as_view(), name='create_book'),
    path('users/update_profile', views.UpdateProfile, name='update_profile'),
    path('comment/delete_comment/<int:pk>', views.DeleteComment, name='delete_comment'),
    path('comment/delete_reply_to_comment/<int:pk>', views.DeleteReplyToComment, name='delete_reply_to_comment'),
    path('movies/delete/<int:pk>', views.deleteMovie, name='delete_movie'),
    path('anime/delete/<int:pk>', views.deleteAnime, name='delete_anime'),
    path('software/delete/<int:pk>', views.deleteSoftware, name='delete_software'),
    path('books/delete/<int:pk>', views.deleteBook, name='delete_book'),

]
