# Generated by Django 3.2.9 on 2022-06-02 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=200)),
                ('product_text', models.CharField(max_length=200)),
                ('product_price', models.IntegerField(default=0)),
                ('cat', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Product.category')),
            ],
        ),
    ]