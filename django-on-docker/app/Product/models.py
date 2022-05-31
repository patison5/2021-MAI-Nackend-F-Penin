from django.db import models
from audioop import reverse

# Сущность категории
# - model: Модель категории
class Category(models.Model):
    category_text = models.CharField(max_length=200)

    def __str__(self):
        return self.category_text
    
    # def get_absolute_url(self):
    #     return reverse('category', kwargs={'category_id': self.pk})

# Сущность продукта
class Product(models.Model):
    product_title = models.CharField(max_length=200)
    product_text = models.CharField(max_length=200)
    product_price = models.IntegerField(default=0)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.product_title