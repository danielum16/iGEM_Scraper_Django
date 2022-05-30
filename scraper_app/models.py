from django.db import models

# Create your models here.
class Team(models.Model):
    url = models.URLField(max_length=200,unique=True)
    abstract = models.TextField()
    team = models.CharField(max_length=254)
    title = models.CharField(max_length=254)
