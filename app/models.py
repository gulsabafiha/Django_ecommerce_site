from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from django.db.models.deletion import CASCADE


STATE_CHOICES=(
    ('Dhaka','Dhaka'), 
    ('Rajshahi','Rajshahi'),
    ('Comilla','Comilla'),
    ('Sylhet','Sylhet'),
    ('Bogra','Bogra'),

)

class Customer(models.Model):
    id = models.BigAutoField(primary_key=True,null=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=20)

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES=(
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top wear'),
    ('BW','Bottom Wear'),
)

class Product(models.Model):
    id = models.BigAutoField(primary_key=True,null=False)
    title=models.CharField(max_length=200)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=200)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image=models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    id = models.BigAutoField(primary_key=True,null=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

STATUS_CHOICES=(
    ('Accepted','Accepted'), 
    ('Paked','Paked'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),

)

class OrderPlaced(models.Model):
    id = models.BigAutoField(primary_key=True,null=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='pending')

    


