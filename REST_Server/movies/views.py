from django.shortcuts import render,get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie,Person
from .serializers import MovieSerializer,PersonSerializer

class MoviesView(APIView):
    def get_all(self):
        try:
            return Movie.objects.all()
        except Movie.DoesNotExist:
            raise Http404
        
    def get(self, request, format=None):
        movies = self.get_all()
        serializer = MovieSerializer(movies, many=True, context={"request": request})
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieView(APIView):
    
    def get_object(self,id):
        return get_object_or_404(Movie, pk=id)
    
#   or
#
#     def get_object(self, pk):
#         try:
#             return Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             raise Http404
        
    def get(self, request, id, format=None):
        movie = self.get_object(id)
        serializer = MovieSerializer(movie, context={"request": request})
        return Response(serializer.data)
    
    def delete(self, request, id, format=None):
        movie = self.get_object(id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, id, format=None):
        movie = self.get_object(id)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonsView(APIView):
    def get_all(self):
        try:
            return Person.objects.all()
        except Person.DoesNotExist:
            raise Http404
        
    def get(self, request, format=None):
        persons = self.get_all()
        serializer = PersonSerializer(persons, many=True, context={"request": request})
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PersonView(APIView):
    
    def get_object(self,id):
        return get_object_or_404(Person, pk=id)
        
    def get(self, request, id, format=None):
        person = self.get_object(id)
        serializer = PersonSerializer(person, context={"request": request})
        return Response(serializer.data)
    
    def delete(self, request, id, format=None):
        person = self.get_object(id)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, id, format=None):
        person = self.get_object(id)
        serializer = PersonSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    