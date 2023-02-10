from django.db import models

# Create your models here.

class Game(models.Model):
    board = models.CharField(max_length=6)
