from django.contrib import admin
from django.contrib import admin

# Register your models here.
from .models import Blog,EmailData
admin.site.register(Blog)

admin.site.register(EmailData)