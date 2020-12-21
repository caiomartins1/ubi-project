# Generated by Django 3.1.3 on 2020-12-21 18:47

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_highlightcard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='country',
        ),
        migrations.AddField(
            model_name='content',
            name='image',
            field=models.ImageField(null=True, upload_to=core.models.content_image_file_path),
        ),
    ]
