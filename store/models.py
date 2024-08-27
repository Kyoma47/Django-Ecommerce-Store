from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category( models.Model ) :
    name = models.CharField( max_length=255, db_index=True )
    slug = models.SlugField( max_length=255, unique=True )  #slug field can't include special characters 

    class Meta :
        verbose_name_plural = 'Categories'
    
    #def get_absolute_url(self):
    #    return reverse("model_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.name

class Product( models.Model ):
    category = models.ForeignKey(
        Category, 
        related_name='product', 
        on_delete=models.CASCADE  # when a category is deleted all matching products will be deleted as well
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default="admin")
    descrition = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField( max_length=255 ) 
    price = models.DecimalField( max_digits=4, decimal_places=2 ) 
    in_stock = models.BooleanField(default=True)
    in_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True) # Will be triggered only once
    updated = models.DateTimeField(auto_now=True) # Will be triggered at each update

    class Meta :
        verbose_name_plural = 'Products'
        ordering = ('-created',) # Ordering when returning the descending order (Last items added first listed)

    def __str__(self):
        return self.title