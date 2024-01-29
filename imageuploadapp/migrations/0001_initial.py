# Generated by Django 5.0.1 on 2024-01-29 06:09

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', tinymce.models.HTMLField(blank=True)),
                ('image', models.ImageField(upload_to='blogs/images/')),
                ('Author', models.CharField(blank=True, max_length=255)),
                ('blogTypeTag', models.CharField(blank=True, max_length=255)),
                ('blogTages', models.JSONField(blank=True, null=True)),
                ('publish', models.BooleanField(default=True)),
                ('featured', models.BooleanField(default=False)),
                ('seo_title', models.CharField(blank=True, max_length=500, null=True)),
                ('meta_description', models.TextField(blank=True, null=True)),
                ('primary_seo_keyword', models.CharField(blank=True, max_length=500, null=True)),
                ('secondary_seo_keywords', models.CharField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmailData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]