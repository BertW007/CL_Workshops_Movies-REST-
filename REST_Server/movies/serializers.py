from rest_framework import serializers
from .models import Movie,Person

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ("title", "description", "director", "actors", "year")
        
class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ("first_name", "last_name")