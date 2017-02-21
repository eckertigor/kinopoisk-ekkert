from kinopoisk_ekkert.models import Film
from rest_framework import serializers


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'
