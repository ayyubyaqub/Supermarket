from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) :
        return str(self.name)

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self) :
        return str(self.name)

class Item(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self) :
        return str(self.name)