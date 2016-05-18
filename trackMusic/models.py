from __future__ import unicode_literals

from django.db import models

class Genre(models.Model):
	genre_name = models.CharField(max_length=200,unique=True)

	def __unicode__(self):
		return self.genre_name


class Track(models.Model):
	track_name = models.CharField(max_length=200,unique=True)
	rating = models.FloatField()

	def __unicode__(self):
		return self.track_name

class TrackGenreMap(models.Model):
	track_id = models.ForeignKey(Track)
	genre_id = models.ForeignKey(Genre)

	class Meta:
		unique_together = ("track_id", "genre_id")

	def __unicode__(self):
		return self.track_id.track_name + " :: " + self.genre_id.genre_name