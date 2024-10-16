from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Books(models.Model):

    status_books =[
        ('available', 'available'),
        ('rental', 'rental'),
        ('sold', 'sold'),
    ]


    title = models.CharField(max_length=250)
    author = models.CharField(max_length=64, null=True, blank=True)
    image = models.ImageField(upload_to='fotos', null=True, blank=True)
    photo_auther = models.ImageField(upload_to='fotos', null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places= 2, null=True, blank=True)
    rental_price = models.DecimalField(max_digits=5, decimal_places= 2, null=True, blank=True)
    rental_period = models.IntegerField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    status =models.CharField(max_length=64, choices=status_books, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)


    def __str__(self):
        return self.title