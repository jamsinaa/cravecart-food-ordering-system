from django.db import models

class Restaurant(models.Model):

    name = models.CharField(max_length=100)

    cuisine = models.CharField(max_length=100)

    rating = models.FloatField()

    image = models.URLField()

    def __str__(self):
        return self.name
    
class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='menu_images/')

    def __str__(self):
        return self.name
    
class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    items = models.TextField()
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
