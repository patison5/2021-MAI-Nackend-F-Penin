from audioop import reverse
import datetime
from django.db import models
from django.utils import timezone

from Users.models import User

# Сущность категории
# - model: Модель категории
class Category(models.Model):
    category_text = models.CharField(max_length=200)

    def __str__(self):
        return self.category_text
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

# Сущность продукта
class Product(models.Model):
    product_title = models.CharField(max_length=200)
    product_text = models.CharField(max_length=200)
    product_price = models.IntegerField(default=0)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    pub_date = models.DateTimeField('date published', default=timezone.now())

    def __str__(self):
        return self.product_title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)




# Product.objects.create(product_title="Плесень", product_text="Описание", product_price=50, cat=b, author=a)
# Product.objects.create(product_title="Молоко", product_text="Описание", product_price=50, cat=b, author=a)
# Category.objects.create(category_text="Для шашлыка")
# Category.objects.create(category_text="Молочка")
# Category.objects.create(category_text="Разное")
# Category.objects.create(category_text="Рыба")

