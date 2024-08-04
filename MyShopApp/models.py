from django.db import models

# for authorization, we use
# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50, default="")
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    description = models.TextField(default="")
    Published_date = models.DateTimeField()
    image = models.ImageField(upload_to="static/shop", default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70, default="")
    phone = models.IntegerField(default="")
    desc = models.TextField(max_length=500, default="")

    def __str__(self):
        return self.name


class Email(models.Model):
    email_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=70, default="") 

    def __str__(self):
        return self.email


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField()
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    phone = models.IntegerField(default=0)
    email = models.CharField(max_length=70, default="")
    address = models.CharField(max_length=200, default="")
    address2 = models.CharField(max_length=200, default="")
    country = models.CharField(max_length=20, default="")
    city = models.CharField(max_length=20, default="")
    zip_code = models.IntegerField(default=0)
    name_on_credit = models.CharField(max_length=50, default="")
    credit_number = models.IntegerField(default=0)
    expiry = models.CharField(max_length=10, default="")
    CVV = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name} Order"


class Order_Update(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    email = models.CharField(max_length=100, default="")
    update_desc = models.CharField(max_length=5000)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
