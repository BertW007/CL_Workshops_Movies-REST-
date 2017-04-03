from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    
    def __str__(self):
        return '{} {}'.format(self.first_name,self.last_name) 

class Movie(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    director = models.ForeignKey(Person,related_name = 'director')
    actors = models.ManyToManyField(Person,through='Role')
    year = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.title)
    
class Role(models.Model):
    person = models.ForeignKey(Person,related_name = 'actor')
    movie = models.ForeignKey(Movie,related_name = 'movie')
    role = models.CharField(max_length=128, null=True)
    
    def __str__(self):
        return '{}'.format(self.role)
