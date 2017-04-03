from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie,Person
from .serializers import MovieSerializer,PersonSerializer

class MoviesView(APIView):
    
    def get_all(self, request, format=None):
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, context={"request": request})
        return Response(serializer.data)