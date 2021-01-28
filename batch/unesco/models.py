from django.db import models

# Create your models here.
class Category(models.Model) :
    name = models.CharField(max_length=128, null=True)

    def __str__(self) :
        return self.name

class State(models.Model) :
    name = models.CharField(max_length=128, null=True)

    def __str__(self) :
        return self.name

class Region(models.Model) :
    name = models.CharField(max_length=128, null=True)

    def __str__(self) :
        return self.name

class Iso(models.Model) :
    name = models.CharField(max_length=128, null=True)

    def __str__(self) :
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    justification = models.TextField()
    year = models.IntegerField(null=True)
    longitude = models.IntegerField(null=True)
    latitude = models.IntegerField(null=True)
    area_hectares = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    states = models.ForeignKey(State, on_delete=models.SET_NULL,null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL,null=True)
    iso = models.ForeignKey(Iso, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name