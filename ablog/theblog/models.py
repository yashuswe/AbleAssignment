from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Posts(models.Model):
    title = models.CharField(max_length = 255)
    title_tag = models.CharField(max_length = 255)
    # image = models.ImageField(upload_to="")
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    body = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    
    def __str__(self):
        return self.title + '|' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')
    
    

# Create your models here.
