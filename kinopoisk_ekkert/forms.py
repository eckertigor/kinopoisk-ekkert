# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django import forms
from kinopoisk_ekkert.models import Film

class UserForm(forms.Form):
	username = forms.CharField(
		required=True,
		widget=forms.TextInput(attrs={'class':'form-control', 'maxlength':20})
	)
	fio = forms.CharField(
		required=True, label=u'ФИО',
		widget=forms.TextInput(attrs={'class':'form-control', 'maxlength':50})
	)
	email = forms.EmailField(
		required=True,
		widget=forms.EmailInput(attrs={'class':'form-control'})
	)
	password = forms.CharField(
		required=True,
		widget=forms.PasswordInput(attrs={'class':'form-control'})
	)
	avatar = forms.FileField(
		required=True, label=u'Загрузите изображение'
	)

class ProfileForm(forms.Form):
	username = forms.CharField(
		widget=forms.TextInput(attrs={'class':'form-control'})
	)
	email = forms.EmailField(
		widget=forms.TextInput(attrs={'class':'form-control'})
	)
	avatar = forms.FileField(
		label='Select a profile Image'
	)

class LoginForm(forms.Form):
	email = forms.EmailField(
		required=True,
		widget=forms.EmailInput(attrs={'class':'form-control', 'required': 'true'})
	)
	password = forms.CharField(
		widget=forms.PasswordInput(attrs={'class':'form-control', 'required': 'true'})
	)

class FilmForm(forms.ModelForm):
	class Meta:
		model = Film
		fields = ['title', 'short_description', 'full_description', 'director',
			'year', 'poster']
	title = forms.CharField(
		required=True, label=u'Название фильма',
		widget=forms.TextInput(attrs={'class':'form-control', 'maxlength':49})
	)
	short_description = forms.CharField(
		required=True, label=u'Краткое описание (160 символов)',
		widget=forms.Textarea(attrs={'class':'form-control',
										'maxlength':160, 'rows':2})
	)
	full_description = forms.CharField(
		required=True, label=u'Полное описание (700 символов)',
		widget=forms.Textarea(attrs={'class':'form-control',
										'maxlength':750, 'rows':6})
	)
	director = forms.CharField(
		required=True, label=u'Режиссер(ы)',
		widget=forms.TextInput(attrs={'class':'form-control', 'maxlength':100})
	)
	year = forms.CharField(
		required=True, label=u'Год выпуска',
		widget=forms.NumberInput(attrs={'class':'form-control', 'maxlength':10})
	)
	poster = forms.FileField(
		required=True, label=u'Выберите обложку фильма'
	)

	def save_film(self, request):
	    film = Film.objects.create(
			title = self.cleaned_data.get('title'),
			short_description = self.cleaned_data.get('short_description'),
			full_description = self.cleaned_data.get('full_description'),
			director = self.cleaned_data.get('director'),
			year = self.cleaned_data.get('year'),
			poster = self.cleaned_data.get('poster'),
			)
	    film.save()
	    return film

class ReviewForm(forms.Form):
	text = forms.CharField(
			widget=forms.Textarea(attrs={'class':'form-control', 'rows': 4,
				'maxlength':500})
	)
