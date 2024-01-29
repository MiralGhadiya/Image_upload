
from django.db import models
from tinymce.models import HTMLField

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = HTMLField(blank=True) 
    image = models.ImageField(upload_to='blogs/images/',null=True, blank=True, max_length=255)
    Author=models.CharField(max_length=255, blank=True)
    blogTypeTag=models.CharField(max_length=255, blank=True)
    blogTages=models.JSONField(null=True, blank=True)
    publish = models.BooleanField(default=True)
    seo_title = models.CharField(max_length=500, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    primary_seo_keyword = models.CharField(
        max_length=500, blank=True, null=True)
    secondary_seo_keywords = models.CharField(
        max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class EmailData(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    subject=models.CharField(max_length=255)
    message=models.TextField()
    email=models.EmailField(max_length=254,null=False)
