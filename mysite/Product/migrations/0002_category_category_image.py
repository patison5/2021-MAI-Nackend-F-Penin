# Generated by Django 4.0.4 on 2022-06-03 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.FileField(default=None, upload_to='media/'),
        ),
    ]