from django.conf.urls import patterns, url, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Kinopoisk-ekkert API')

urlpatterns = patterns(
    'kinopoisk_ekkert.views',
    url(r'^filmsList/(?P<sort>\w+)$', 'films_list', name='films_list'),
    url(r'^film/(?P<pk>[0-9]+)$', 'film_detail', name='film_detail'),
    url(r'^docs/', schema_view),
)
