#from __future__ import unicode_literals

from django.db import models

# Create your models here.
class checkout(models.Model):

    Country_Choices = (
        ('IN', 'India'),
        ('US', 'United States'),
        ('CH', 'China'),
        ('UK', 'United kingdom')
    )
    
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    email = models.EmailField()
    country = models.CharField(max_length=2,
                               choices=Country_Choices,
                               null=True)
    address = models.CharField(max_length=30)
    town = models.CharField(max_length=30)
    zip_code = models.IntegerField()
    ph_number = models.IntegerField()
    comment = models.TextField(null=True)

    def __unicode__(self):
        return self.fname



class Categories(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)
    

    def __unicode__(self):
        return self.name
    
class Product(models.Model):
    category=models.ForeignKey(Categories)
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,null=True)

    #change in settings.py and urls.py for pic
    
    description = models.TextField(blank=True)
    pic = models.FileField(upload_to = 'pic',null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __unicode__(self):
        return self.name

class Cart(models.Model):
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    total_price = models.FloatField()

    def __unicode__(self):
        return self.product.name
