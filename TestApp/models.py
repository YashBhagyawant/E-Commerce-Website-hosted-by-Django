from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return self.name;

class Shop(models.Model):
    Item_name = models.CharField(max_length=25)
    Price = models.IntegerField()
    Image = models.ImageField(upload_to='Shop/')
    def __str__(self):
        return self.Item_name;
