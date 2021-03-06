# Generated by Django 3.1 on 2022-04-29 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Men',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mens_category_name', models.CharField(max_length=50, unique=True)),
                ('mens_slug', models.SlugField(max_length=100, unique=True)),
                ('mens_description', models.TextField(blank=True, max_length=250)),
                ('mens_category_img', models.ImageField(blank=True, upload_to='photos/category')),
            ],
        ),
    ]
