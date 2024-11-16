from django.db import models

# Create your models here.


class product(models.Model):
    prod_name = models.CharField(max_length=100)
    prod_price = models.IntegerField()
    prod_category = models.CharField(max_length=100)
    prod_qnty = models.IntegerField()
    prod_img = models.ImageField(upload_to='products/')
    prod_desc = models.CharField(max_length=50)

#anytime you make changes to the model you Must make and run migrations