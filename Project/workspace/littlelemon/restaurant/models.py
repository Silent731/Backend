from django.db import models

# Create your models here.
class Menu(models.Model):
    Title = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    inventory = models.SmallIntegerField()
    
    def __str__(self):
        return f'{self.Title}: (str{self.price})'
class Booking(models.Model):
    name = models.CharField(max_length=255)
    No_of_guest = models.SmallIntegerField()
    BookingDate = models.DateTimeField(null=False)

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length= 250, db_index = True)



