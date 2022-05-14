# Generated by Django 4.0.4 on 2022-05-14 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
        ('Product', '0002_product_authors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='authors',
        ),
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Users.user'),
        ),
    ]