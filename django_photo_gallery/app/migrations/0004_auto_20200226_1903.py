# Generated by Django 2.2.10 on 2020-02-26 16:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200226_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.TextField(max_length=510),
        ),
        migrations.AlterField(
            model_name='album',
            name='tags',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='albumimage',
            name='slug',
            field=models.SlugField(default=uuid.uuid4, editable=False, max_length=71),
        ),
    ]