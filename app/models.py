from django.db import models

# Create your models here.

CATEGORY_CHOICES=(
    ('PO','Pottery'),
    ('NE','Needleworks'),
    ('JE','Jewels'),
    ('PA','Paintings'),
    ('DE','Decorations'),
)


class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    composition=models.TextField(default='')
    prodapp=models.TextField(default='')
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image=models.ImageField(upload_to='product')

    def __str__(self):
        return self.title
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True) total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    class CartItem(models.Model):
        cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
        product = models.ForeignKey('Product', on_delete=models.CASCADE) quantity = models.PositiveIntegerField()
        price = models.DecimalField(max_digits=10, decimal_places=2) 
        class Product(models.Model):
            name = models.CharField(max_length=100)
            price = models.DecimalField(max_digits=10, decimal_places=2)
class Order(models.Model):
    fullname = models.CharField(max_length=100) phone = models.CharField(max_length=15) email = models.EmailField()
    pincode = models.PositiveIntegerField() address = models.TextField()
    class Product(models.Model):
        name = models.CharField(max_length=100)
        price = models.DecimalField(max_digits=10, decimal_places=2) image = models.ImageField(upload_to='products/')
