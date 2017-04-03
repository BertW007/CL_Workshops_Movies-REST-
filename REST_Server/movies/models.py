from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    
    def __str__(self):
        return '{} {}'.format(self.first_name,self.last_name) 

class Movie(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    director = models.ForeignKey(Person)
    actors = models.ManyToManyField(Person,through='Role')
    year = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.title)
