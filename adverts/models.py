from __future__ import unicode_literals

from django.db import models

class Advert(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')
    description = models.CharField(max_length=1023)
    author_name = models.CharField(max_length=127)
    phone_number = models.CharField(max_length=56)
    price = models.BigIntegerField()
    views = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class Country(models.Model):
    name = models.CharField(max_length=255)

class CountryTranslation(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    language = models.CharField(max_length=56)
    name = models.CharField(max_length=255)

class District(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class DistrictTranslation(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    language = models.CharField(max_length=56)
    name = models.CharField(max_length=255)

class City(models.Model):

    
class CityTranslation(models.Model):

class Image(models.Model):

class Type(models.Model):

class TypeTranslation(models.Model):

class AdvertComfort(models.Model):

class Comfort(models.Model):

class ComfortTranslation(models.Model):