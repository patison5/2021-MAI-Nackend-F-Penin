from django.db import models

# Сущность продукта
class User(models.Model):
    user_name = models.CharField(max_length=200)
    user_surname = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)
    user_login = models.CharField(max_length=200)

    def __str__(self):
        return self.user_login