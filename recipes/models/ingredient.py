from django.db import models

class Ingredient(models.Model):

    class Type(models.TextChoices):
        PRODUCE = 'PR'
        GRAINS = 'GR'
        CANNED = 'CA'
        HERB_SPICE = 'HS'
        DAIRY = 'DA'
        MEAT = 'ME'
        SEAFOOD = 'SE'
        MISCELLANEOUS = 'MI'

    name = models.CharField()
    type = models.CharField(choices=Type.choices)
    fdc_id = models.IntegerField()  # Used to access info on USDA api
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE, related_name='recipe_ingredients')
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='recipe_ingredients')
    measurement = models.ForeignKey('Measurement', on_delete=models.SET_NULL, related_name='ingredients')
    quantity = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)