from django.db import models


# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(blank=False, upload_to='instagram/%Y/%m/%d')
    contents = models.TextField()
    cdate = models.DateTimeField(auto_now_add=True)
