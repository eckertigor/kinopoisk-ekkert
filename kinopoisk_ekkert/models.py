from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib import auth


class Profile(models.Model):
	avatar = models.FileField()
	nickname = models.CharField(max_length = 20)
	fio = models.CharField(max_length = 50)


class Film(models.Model):
	title = models.CharField(max_length = 49)
	short_description = models.CharField(max_length = 160)
	full_description = models.CharField(max_length = 750)
	director = models.CharField(max_length = 100)
	year = models.IntegerField()
	rating = models.FloatField(default = 0)
	is_deleted = models.IntegerField(default = 0)
	add_date = models.DateTimeField(auto_now_add=True)
	poster = models.FileField(default = 0)


class Rate(models.Model):
	value = models.IntegerField()
	user = models.CharField(max_length = 30)
	film = models.IntegerField()


class Review(models.Model):
	user = models.CharField(max_length = 30)
	user_avatar = models.CharField(max_length = 30, default = 0)
	film = models.IntegerField()
	text = models.CharField(max_length = 500)
	is_banned = models.IntegerField(default = 0)
