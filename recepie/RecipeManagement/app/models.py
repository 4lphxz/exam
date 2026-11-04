from django.db import models

#
# - `recipename` – CharField
# - `instructions` – TextField
# - `ingredients` – TextField
# - `mealtype` – CharField
# - `cuisine` – CharField
# - `image` – ImageField

class Recipe(models.Model):
    recipename = models.CharField(max_length=20)
    instructions = models.CharField(max_length=2000)
    ingredients = models.CharField(max_length=2000)
    mealtype = models.CharField(max_length=20)
    cuisine = models.CharField(max_length=20)
    image=models.ImageField(upload_to="Recepie",null=True)
