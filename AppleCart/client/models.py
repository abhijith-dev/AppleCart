from django.db import models
from django.db import models
from django.db import IntegrityError
class User(models.Model):
    user_id=models.AutoField
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    objects=models.Manager()
    def __str__(self):
        return self.email
class Item(models.Model):
    item_name=models.CharField(max_length=50)
    item_id=models.AutoField
    price=models.IntegerField()
    item_p=models.IntegerField(default=0)
    item_desc=models.CharField(max_length=100)
    item_catagory=models.CharField(max_length=100,default="")
    item_image=models.ImageField(upload_to="images/client/",default="")
    objects=models.Manager()
    def __str__(self):
        return self.item_name
class AppleCartadmin(models.Model):
    email=models.CharField(max_length=60)
    password=models.CharField(max_length=50)
    objects=models.Manager()
    def __str__(self):
        return self.email
class Order(models.Model):
    user_name=models.CharField(max_length=50)
    user_email=models.CharField(max_length=60)
    user_number=models.CharField(max_length=60)
    area=models.CharField(max_length=60)
    quantity=models.IntegerField(default=0)
    city=models.CharField(max_length=60)
    Landmark=models.CharField(max_length=60)
    pincode=models.IntegerField()
    district=models.CharField(max_length=60)
    state=models.CharField(max_length=60)
    item_name=models.CharField(max_length=60)
    item_price=models.CharField(max_length=60)
    item_desc=models.CharField(max_length=60)
    order_date=models.CharField(max_length=60)
    order_time=models.CharField(max_length=60,default=0)
    delivery_date=models.CharField(max_length=50 ,default=0)
    objects=models.Manager()
    def __str__(self):
        return self.user_email       
