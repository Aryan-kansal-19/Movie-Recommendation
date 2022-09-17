from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_movie, name = 'home'),
    path("index_movie/", views.index_movie, name="index_movie"),
    path("index_tv/", views.index_tv, name="index_tv"),
    path("search/", views.search, name="search"),
    path("tv_details/<int:tv_id>/", views.view_tv_detail, name = "tv-details"),
    path("movie_details/<int:movie_id>/", views.view_movie_detail, name = "movie-details"),
]
