from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Track, Genre, TrackGenreMap
from .forms import AddTrackForm, AddGenreForm
from django.template import loader
from .search import get_query
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return HttpResponseRedirect('trackmusic/tracks')


def tracks(request):
    track_list = Track.objects.order_by('rating')[::-1]
    if 'page' in request.GET:
        page = request.GET['page']
        paginator = Paginator(track_list,5)
        try:
            tracks = paginator.page(page)
        except PageNotAnInteger:
            tracks = paginator.page(1)
        except EmptyPage:
            tracks = paginator.page(paginator.num_pages)
    else:
        paginator = Paginator(track_list,5)
        tracks = paginator.page(1)
    context = {'track_list': tracks}
    return render(request, 'trackMusic/index.html', context)


def trackDetail(request, track_id):
    track = get_object_or_404(Track, pk=track_id)
    return render(request, 'trackMusic/track_detail.html', {'track':track})


def genres(request):
    genre_list = Genre.objects.all()
    if 'page' in request.GET:
        page = request.GET['page']
        paginator = Paginator(genre_list,5)
        try:
            genres = paginator.page(page)
        except PageNotAnInteger:
            genres = paginator.page(1)
        except EmptyPage:
            genres = paginator.page(paginator.num_pages)
    else:
        paginator = Paginator(genre_list,5)
        genres = paginator.page(1)
    return render(request, 'trackMusic/genres.html', {'genre_list':genres})


def genre_detail(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    return render(request, 'trackMusic/genre_detail.html', {'genre':genre})


def addTrack(request):

    message = ""
    if request.method == 'POST':
        form = AddTrackForm(request.POST)
        if form.is_valid():
            track_name = form.cleaned_data['track_name']
            track_rating = form.cleaned_data['track_rating']
            genre = form.cleaned_data['genre']
            track = Track(track_name = track_name, rating=int(track_rating))
            track.save()

            for g in genre:
                trackgenremap = TrackGenreMap(track_id=track, genre_id=g)
                trackgenremap.save()
            message = "Great! Track Added Successfully."
    else:
        form = AddTrackForm()
    return render(request, 'trackMusic/addtrack.html',{'form':form, 'message':message})


def editTrack(request, track_id):
    return HttpResponse("genre detail will be shown here")


def addGenre(request):
    message= ""
    if request.method == 'POST':
        form = AddGenreForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Great! Genre Added Successfully"
    else:
        form = AddGenreForm()
    return render(request, 'trackMusic/addgenre.html',{'form':form, 'message':message})


def editGenre(request, genre_id):
    return HttpResponse("genre detail will be shown here")


def searchTracks(request):
    query_string = ''
    found_entries = None
    search_fields=('track_name','rating')

    if ('q' in request.GET) and request.GET['q'].strip():

        query_string = request.GET['q']

        entry_query = get_query(query_string, search_fields)
        print entry_query
        found_entries = Track.objects.filter(entry_query)

        return render(request, 'trackMusic/index.html',
                         {'query_string': query_string, 'track_list': found_entries })

def searchGenres(request):
    query_string = ''
    found_entries = None
    search_fields=['genre_name']

    if ('q' in request.GET) and request.GET['q'].strip():

        query_string = request.GET['q']

        entry_query = get_query(query_string, search_fields)
        print entry_query
        found_entries = Genre.objects.filter(entry_query)

        return render(request, 'trackMusic/genres.html',
                         {'query_string': query_string, 'genre_list': found_entries })

