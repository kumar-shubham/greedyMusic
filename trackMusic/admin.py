from django.contrib import admin

from .models import Genre, Track,TrackGenreMap

# Register your models here.

admin.site.register(Track)
admin.site.register(Genre)
admin.site.register(TrackGenreMap)
