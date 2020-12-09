from django.db import models

# Create your models here.

#model for product
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images",default="")

    #use to store data in wrt name of product
    def __str__(self):
        return self.product_name

#model for contact
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70,default="")
    email = models.CharField(max_length=70,default="")
    phone = models.IntegerField(max_length=70,default="")
    desc = models.CharField(max_length=1000,default="")

    def __str__(self):
        return self.name