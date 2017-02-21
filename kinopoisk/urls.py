from django.conf.urls import include, url
from django.contrib import admin
from kinopoisk_ekkert import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'kinopoisk.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name = 'index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rating/', views.rating, name = 'rating'),
    url(r'^login/$', views.login, name = 'login'),
    url(r'^vote/$', views.vote, name = 'vote'),
    url(r'^api/', include('kinopoisk_ekkert.urls')),
    url(r'^date/$', views.date, name = 'date'),
    url(r'^title/$', views.title, name = 'title'),
    url(r'^popular/$', views.popular, name = 'popular'),
    url(r'^review/$', views.review, name = 'review'),
    url(r'^profile/$', views.profile, name = 'profile'),
    url(r'^control/$', views.control, name = 'control'),
    url(r'^control/add/$', views.add_film, name = 'add_film'),
    url(r'^signup/?', views.signup, name = 'signup'),
    url(r'^logout/?', views.logout, name = 'logout'),
    url(r'^film/(?P<film_id>\d+)?/?', views.film, name = 'film'),
    url(r'^control/edit/(?P<film_id>\d+)?/?', views.edit_film, name = 'edit'),
    url(r'^control/delete/(?P<film_id>\d+)?/?', views.delete_film, name = 'delete'),
    url(r'^control/hide/(?P<review_id>\d+)?/?(?P<type>\d+)?/?', views.hide_review, name = 'hide'),
    url(r'^control/restore/(?P<film_id>\d+)?/?', views.restore_film, name = 'restore'),
]
