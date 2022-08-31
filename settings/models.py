from django.db import models

# Create your models here.

class About(models.Model):
    BlogName = models.CharField(max_length=100)
    image =models.ImageField(upload_to='about')
    subtitle= models.TextField(max_length=500)
    aboutme= models.TextField(max_length=10000)
    tw_account =models.URLField()
    fb_account =models.URLField()
    ins_account =models.URLField()
    link_account =models.URLField()
