# Generated by Django 4.2.3 on 2023-07-19 03:42

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='posts/default.PNG', upload_to=blog.models.upload_to, verbose_name='Image'),
        ),
    ]
