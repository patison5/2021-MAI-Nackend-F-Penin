from django.db import models

# Сущность продукта
class User(models.Model):
    user_name = models.CharField(max_length=200)
    user_surname = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)
    user_login = models.CharField(max_length=200)

    def __str__(self):
        return self.user_login


# User.objects.create(user_name="Fedor", user_surname="Penin", user_email="patison4@yandex.ru", user_login="patison5")
# User.objects.create(user_name="NeFedor", user_surname="NePenin", user_email="patison55@yandex.ru", user_login="patison55")