from django.conf.urls import url
from . import views

app_name = 'trackmusic'
urlpatterns =  [
	url(r'^$', views.index, name='index'),
	url(r'^trackmusic/^$', views.index, name='index1'),
	url(r'^trackmusic/tracks$', views.tracks, name='tracks'),
	url(r'^trackmusic/tracks/([0-9]+)$', views.trackDetail, name='trackDetail'),
	url(r'^trackmusic/genres$', views.genres, name='genres'),
	url(r'^trackmusic/genres/([0-9]+)$', views.genre_detail, name='genre_detail'),
	url(r'^trackmusic/tracks/add$', views.addTrack, name='addTrack'),
	url(r'^trackmusic/tracks/edit/([0-9]+)$', views.editTrack, name='editTrack'),
	url(r'^trackmusic/genres/add$', views.addGenre, name='addGenre'),
	url(r'^trackmusic/genres/edit/([0-9]+)$', views.editGenre, name='editGenre'),
    url(r'^trackmusic/tracks/search$', views.searchTracks, name='searchTrack'),
    url(r'^trackmusic/genres/search$', views.searchGenres, name='searchGenre')

]