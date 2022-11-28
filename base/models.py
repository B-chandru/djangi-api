from django.db import models

class Item(models.Model):
    username= models.CharField(max_length=50)
    quotes = models.TextField()
    tags = models.CharField( max_length=50)
    created = models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return self.username