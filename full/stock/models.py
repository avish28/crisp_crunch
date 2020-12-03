from django.db import models

# Create your models here.

class stock_table(models.Model):
    brand=models.CharField(max_length=100,blank=True)
    product=models.CharField(max_length=100)
    qty=models.IntegerField()
    rate=models.IntegerField()
    gst=models.IntegerField()

    def __str__(self):
        return f"{self.brand}={self.product}={self.qty}"
