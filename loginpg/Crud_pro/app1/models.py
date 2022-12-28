from django.db import models

# Create your models here.
class Order(models.Model):
    oid=models.IntegerField()
    product_name=models.CharField(max_length=100)
    quantity=models.IntegerField()
    del_date=models.DateField()
    price=models.FloatField()
    address=models.CharField(max_length=250)
    phone=models.CharField(max_length=12)