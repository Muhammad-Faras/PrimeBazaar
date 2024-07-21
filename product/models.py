from django.db import models
from django.contrib.auth.models import User
class MainCategoryModel(models.Model):
    main_category_name = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)
    class Meta:
        ordering = ['-created_date'] 

    def __str__(self):
        return self.main_category_name
    
    
class SubCategoryModel(models.Model):
    main_category = models.ForeignKey(MainCategoryModel,on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='subcategory_images/', null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    class Meta:
        ordering = ['-created_date'] 

    def __str__(self):
        return f'{self.sub_category_name} -> {self.main_category.main_category_name}'
    
class Color(models.Model):
    color_name = models.CharField(max_length=50)

    def __str__(self):
        return self.color_name
    

class Product(models.Model):
    sub_category = models.ForeignKey(SubCategoryModel, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    colors = models.ManyToManyField(Color, blank=True)
    def __str__(self):
        return self.name
    

class Laptop(Product):
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    screen_size = models.CharField(max_length=20)
    hard_disk_size = models.CharField(max_length=20)
    cpu_model = models.CharField(max_length=100)
    ram_memory = models.CharField(max_length=50)
    operating_system = models.CharField(max_length=50)
    special_feature = models.TextField()
    graphic_card = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.brand} {self.model_name}"

class Nintendo(Product):
    brand = models.CharField(max_length=100 ,null=True, blank=True )
    model_name = models.CharField(max_length=100 ,null=True, blank=True )
    memory_storage_capacity = models.CharField(max_length=20 ,null=True, blank=True )
    flash_memory_type = models.TextField(null=True, blank=True )
    compatible_devices = models.TextField(null=True, blank=True )

    def __str__(self):
        return f"{self.name} -> {self.sub_category.sub_category_name}"

    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart of {self.user.username}"
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"