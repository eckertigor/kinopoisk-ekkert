# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Avg, Count
from kinopoisk_ekkert.models import Profile, Film, Rate, Review
from django.shortcuts import redirect
from django.contrib import auth
from django.http import HttpResponseRedirect, Http404, JsonResponse
from kinopoisk_ekkert.forms import UserForm, ProfileForm, LoginForm, FilmForm, ReviewForm
from django.contrib.auth.models import User
from django.template import RequestContext
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from kinopoisk_ekkert.serializers import FilmSerializer
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage
from django.core.files import File
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import EmptyPage, PageNotAnInteger
import json

def index(request):
    films = Film.objects.filter(is_deleted=0).order_by('-rating')
    if request.user.is_authenticated():
        profile = Profile.objects.get(nickname=request.user.username)
        avatar = profile.avatar.name[2:]
        return render(request, 'index.html', { 'avatar' : avatar,
                                                    'films' : films})
    return render(request, 'index.html', {'films' : films})


def rating(request):
    films = Film.objects.filter(is_deleted=0).order_by('-rating')
    if request.user.is_authenticated():
        profile = Profile.objects.get(nickname=request.user.username)
        avatar = profile.avatar.name[2:]
        return render(request, 'rating.html', { 'avatar' : avatar,
                                                    'films' : films})
    return render(request, 'rating.html', {'films' : films})


def popular(request):
    rating = Rate.objects.values_list('film',flat=True).annotate(total=Count('film')).order_by('-total')
    rat_list = list(rating)
    clauses = ' '.join(['WHEN id=%s THEN %s' % (pk, i) for i, pk in enumerate(rat_list)])
    ordering = 'CASE %s END' % clauses
    filmset = Film.objects.filter(pk__in=rat_list, is_deleted=0).extra(
           select={'ordering': ordering}, order_by=('ordering',))
    if request.user.is_authenticated():
        profile = Profile.objects.get(nickname=request.user.username)
        avatar = profile.avatar.name[2:]
        return render(request, 'popular.html', { 'avatar' : avatar,
                                                    'films' : filmset})
    return render(request, 'popular.html', {'films' : filmset})


def title(request):
    films = Film.objects.filter(is_deleted=0).order_by('title')
    if request.user.is_authenticated():
        profile = Profile.objects.get(nickname=request.user.username)
        avatar = profile.avatar.name[2:]
        return render(request, 'title.html', { 'avatar' : avatar,
                                                    'films' : films})
    return render(request, 'title.html', {'films' : films})


def date(request):
    films = Film.objects.filter(is_deleted=0).order_by('-add_date')
    if request.user.is_authenticated():
        profile = Profile.objects.get(nickname=request.user.username)
        avatar = profile.avatar.name[2:]
        return render(request, 'date.html', { 'avatar' : avatar,
                                                    'films' : films})
    return render(request, 'date.html', {'films' : films})


def api(request, films):
    if request.GET.get('sort') == 'date':
        return date(request)
    if request.GET.get('sort') == 'popular':
        return popular(request)
    if request.GET.get('sort') == 'rating':
        return index(request)
    if request.GET.get('sort') == 'title':
        return title(request)


def film(request, film_id):
    try:
        film = Film.objects.get(id=film_id)
    except Film.DoesNotExist:
        raise Http404
    try:
        reviews = Review.objects.filter(film=film_id)
    except Review.DoesNotExist:
        reviews = None
    stars = []
    for i in range (1, 11):
        result = Rate.objects.filter(film=film_id, value=i).count()
        stars.insert(i, result)
    form = ReviewForm()
    if film.is_deleted == 1 and not request.user.is_superuser:
        raise Http404
    if request.user.is_authenticated():
        profile = Profile.objects.get(nickname=request.user.username)
        avatar = profile.avatar.name[2:]
        try:
            my_rating = Rate.objects.get(user=request.user.username, film=film_id)
        except Rate.DoesNotExist:
            my_rating = Rate()
            my_rating.value = 0
        return render(request, 'film.html',
            { 'avatar' : avatar, 'film' : film, 'form' : form,
                    'my_rating' : my_rating.value, 'reviews' : reviews,
                                                            'stars' : stars})
    return render(request, 'film.html', {'film' : film, 'form' : form,
                    'reviews' : reviews, 'stars' : stars})


def login(request):
    if request.user.is_authenticated():
        return redirect('/')
    if request.method == 'POST':
        response_data = {}
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            userByEmail = User.objects.get(email=email)
        except User.DoesNotExist:
            response_data['error'] = u'Пользователь с таким email не найден'
            return JsonResponse(response_data)
        user = auth.authenticate(username=userByEmail.username, password=password)
        if user is not None:
            auth.login(request, user)
            profile = Profile.objects.get(nickname=userByEmail.username)
            response_data['avatar'] = profile.avatar.name[2:]
            response_data['result'] = u'Вы успешно авторизировались'
            response_data['user'] = userByEmail.username
            return JsonResponse(response_data)
        else:
            response_data['error'] = u'Проверьте правильность введенных данных'
            return JsonResponse(response_data)
    else:
        form = LoginForm()
        return render(request, 'login.html', { 'form' : form })


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def signup(request):
    if request.method == 'POST':
        response_data = {}
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            fio = form.cleaned_data.get('fio')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            avatar = form.cleaned_data.get('avatar')
            if User.objects.filter(username=username).exists():
                response_data['error'] = u'Пользователь с таким username уже существует'
                return JsonResponse(response_data)
            if User.objects.filter(email=email).exists():
                response_data['error'] = u'Пользователь с таким email уже существует'
                return JsonResponse(response_data)
            u = User.objects.create_user(username, email, password)
            p = Profile.objects.create(nickname=username,
                                avatar=request.FILES['avatar'], fio=fio)
            p.save()
            response_data['result'] = u'Вы успешно зарегестрировались'
            response_data['button'] = u'Войти?'
            return JsonResponse(response_data)
        else:
            response_data['error'] = u'Проверьте введенные данные'
            return JsonResponse(response_data)
    else:
        form = UserForm()
        return render(request, 'signup.html', { 'form' : form })


def profile(request):
    if request.user.is_authenticated():
        profile = Profile.objects.get(nickname=request.user.username)
        avatar = profile.avatar.name[2:]
        stars = []
        films = Film.objects.filter(is_deleted=0)
        for i in range (1, 11):
            result = Rate.objects.filter(value=i, user=request.user.username,
                                                        film__in=films).count()
            stars.insert(i, result)
        return render(request, 'profile.html', { 'avatar' : avatar,
                                                    'stars' : stars})
    else:
        return redirect('/')


def control(request):
    if request.user.is_superuser:
        profile = Profile.objects.get(nickname=request.user.username)
        avatar = profile.avatar.name[2:]
        films = Film.objects.all()
        return render(request, 'control.html', { 'avatar' : avatar,
                                                        'films' : films})
    return redirect('/')


@user_passes_test(lambda u: u.is_superuser)
def add_film(request):
    if request.method == 'POST':
        response_data = {}
        filmForm = FilmForm(request.POST, request.FILES)
        if filmForm.is_valid():
            filmForm.save_film(request)
            response_data['result'] = u'Фильм успешно добавлен!'
            response_data['button'] = u'Вернуться в панель управления?'
            return JsonResponse(response_data)
        else:
            response_data['error'] = u'Проверьте правильность введенных данных'
            return JsonResponse(response_data)
    else:
        form = FilmForm()
        profile = Profile.objects.get(nickname=request.user.username)
        avatar = profile.avatar.name[2:]
        return render(request, 'add.html', { 'form' : form, 'avatar' : avatar })


@user_passes_test(lambda u: u.is_superuser)
def edit_film(request, film_id):
    film = Film.objects.get(id=film_id)
    # old_d = film.add_date
    if request.method == 'POST':
        response_data = {}
        filmForm = FilmForm(request.POST, request.FILES, instance=film)
        if filmForm.is_valid():
            filmForm.save()
            # film.add_date = old_d
            # film.save()
            response_data['result'] = u'Фильм успешно изменен'
            response_data['button'] = u'Вернуться в панель управления?'
            return JsonResponse(response_data)
        else:
            response_data['error'] = u'Проверьте правильность введенных данных'
            return JsonResponse(response_data)
    else:
        form = FilmForm(initial=
            {'title': film.title, 'short_description': film.short_description,
                'full_description': film.full_description, 'director': film.director,
                    'year': film.year, 'poster': film.poster})
        profile = Profile.objects.get(nickname=request.user.username)
        avatar = profile.avatar.name[2:]
        return render(request, 'edit.html',
                        { 'form' : form, 'avatar' : avatar, 'film' : film })


@user_passes_test(lambda u: u.is_superuser)
def delete_film(request, film_id):
    if request.method == 'POST':
        response_data = {}
        film = Film.objects.get(id=film_id)
        film.is_deleted = 1
        film.save()
        response_data['result'] = 'success'
        response_data['film_id'] = film.id
        response_data['film_title'] = film.title
        return JsonResponse(response_data)


@user_passes_test(lambda u: u.is_superuser)
def restore_film(request, film_id):
    if request.method == 'POST':
        response_data = {}
        film = Film.objects.get(id=film_id)
        film.is_deleted = 0
        film.save()
        response_data['result'] = 'success'
        response_data['film_id'] = film.id
        response_data['film_title'] = film.title
        return JsonResponse(response_data)


@user_passes_test(lambda u: u.is_superuser)
def hide_review(request, review_id, type):
    if request.method == 'POST':
        response_data = {}
        review = Review.objects.get(id=review_id)
        review.is_banned = type
        review.save()
        response_data['result'] = 'success'
        response_data['review'] = review_id
        return JsonResponse(response_data)


@login_required
def vote(request):
    if request.method == 'POST':
        response_data = {}
        film_id=request.POST.get('film_id')
        Rate.objects.filter(film=film_id, user=request.user.username).delete()
        rate = Rate.objects.create(value=request.POST.get('value'),
                user=request.user.username, film=film_id)
        rate.save()
        rating_new = Rate.objects.values('value').filter(film=film_id). \
                                    aggregate(Avg('value')).get('value__avg')
        film = Film.objects.get(id=film_id)
        film.rating = rating_new
        film.save()
        response_data['status'] = 'ok'
        response_data['rating'] = rating_new
        return JsonResponse(response_data)


@login_required
def review(request):
    if request.method == 'POST':
        response_data = {}
        film_id = request.POST.get('film_id')
        text = request.POST.get('text')
        profile = Profile.objects.get(nickname=request.user.username)
        avatar = profile.avatar.name[2:]
        review = Review.objects.create(film=film_id, user=request.user.username,
                text=text, user_avatar = avatar)
        review.save()
        response_data['status'] = 'ok'
        return JsonResponse(response_data)

@api_view(['GET'])
def films_list(request, sort):
    if request.method == 'GET':
        if sort == 'rating':
            films = Film.objects.filter(is_deleted=0).order_by('-rating')
        elif sort == 'title':
            films = Film.objects.filter(is_deleted=0).order_by('title')
        elif sort == 'popular':
            rating = Rate.objects.values_list('film',flat=True).annotate(
                                        total=Count('film')).order_by('-total')
            rat_list = list(rating)
            clauses = ' '.join(['WHEN id=%s THEN %s' % (pk, i) for i, pk in enumerate(rat_list)])
            ordering = 'CASE %s END' % clauses
            films = Film.objects.filter(pk__in=rat_list, is_deleted=0).extra(
                   select={'ordering': ordering}, order_by=('ordering',))
        elif sort == 'date':
                films = Film.objects.filter(is_deleted=0).order_by('-add_date')
        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def film_detail(request, pk):
    try:
        film = Film.objects.get(id=pk)
    except Film.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        stars = {}
        for i in range (1, 11):
            result = Rate.objects.filter(film=pk, value=i).count()
            stars[i] = result
        serializer = FilmSerializer(film)
        data = serializer.data
        data['rates'] = stars
        return Response(data)


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
