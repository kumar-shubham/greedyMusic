from django.conf.urls import url
from . import views

app_name = 'trackmusic'
urlpatterns =  [
	url(r'^$', views.index, name='index'),
	url(r'^tracks$', views.tracks, name='tracks'),
	url(r'^tracks/([0-9]+)$', views.trackDetail, name='trackDetail'),
	url(r'^genres$', views.genres, name='genres'),
	url(r'^genres/([0-9]+)$', views.genre_detail, name='genre_detail'),
	url(r'^tracks/add$', views.addTrack, name='addTrack'),
	url(r'^tracks/edit/([0-9]+)$', views.editTrack, name='editTrack'),
	url(r'^genres/add$', views.addGenre, name='addGenre'),
	url(r'^genres/edit/([0-9]+)$', views.editGenre, name='editGenre'),
    url(r'^tracks/search$', views.searchTracks, name='searchTrack'),
    url(r'^genres/search$', views.searchGenres, name='searchGenre')

]