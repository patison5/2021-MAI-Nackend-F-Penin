from audioop import reverse
import datetime
from django.db import models
from django.utils import timezone

from Users.models import User

# Сущность категории
# - model: Модель категории
class Category(models.Model):
    category_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.category_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

# Сущность продукта
class Product(models.Model):
    product_title = models.CharField(max_length=200)
    product_text = models.CharField(max_length=200)
    product_price = models.IntegerField(default=0)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    authors = models.ManyToManyField(User)

    def __str__(self):
        return self.product_title