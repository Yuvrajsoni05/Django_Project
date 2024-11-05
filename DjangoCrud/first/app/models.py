from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    quality = models.CharField(max_length=50)
    product_type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    manufacture_date = models.DateField()
    available = models.BooleanField(default=False)
    rating = models.IntegerField(default=1)

    class Meta:
        ordering = ['id']
