from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    image = models.ImageField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(blank=True)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Business(Product):
    pass