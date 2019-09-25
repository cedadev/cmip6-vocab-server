from django.db import models


# Create your models here.
class Concept(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    prefLabel = models.CharField(max_length=1500)
    notation = models.CharField(max_length=100)
    definition = models.CharField(max_length=1500, blank=True, default='')

    class Meta:
        ordering = ('prefLabel',)

    def __str__(self):
        return self.prefLabel


class Collection(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    prefLabel = models.CharField(max_length=100)
    definition = models.CharField(max_length=300, blank=True, default='')
    members = models.ManyToManyField(Concept)

    class Meta:
        ordering = ('prefLabel',)

    def __str__(self):
        return self.prefLabel


class Vocab(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    prefLabel = models.CharField(max_length=100)
    definition = models.CharField(max_length=300, blank=True, default='')
    collections = models.ManyToManyField(Collection)

    def __str__(self):
        return self.prefLabel
