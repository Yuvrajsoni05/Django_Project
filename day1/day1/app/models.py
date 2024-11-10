from django.db import models

# Create your models here.
class Crud_Data(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    

