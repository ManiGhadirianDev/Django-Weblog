from django.db import models

# Create your models here.
class Post(models.Model):
    # image
    # author
    title= models.CharField(max_length=150)
    content= models.TextField()
    # tag 
    # categori
    counted_view=models.IntegerField(default=0)
    status = models.BooleanField()
    publushed_date=models.DateTimeField()   
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
