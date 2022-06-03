from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = 'my_category'

    name = models.CharField(max_length=70)
    description = models.TextField(max_length=256)

class Drink(models.Model):
    class Meta:
        db_table = 'my_drink'

    name = models.CharField(max_length=70)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    nutrition = models.CharField(max_length=70)
