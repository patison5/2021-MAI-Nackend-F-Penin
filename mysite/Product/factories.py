import factory
from . import models
import random
from faker import Faker

fake = Faker()
faker = Faker(locale="Ru_ru")

class ProductFactory(factory.Factory):
    class Meta:
        model = models.Product

    # product_title = factory.Faker('bank')
    # product_text = factory.Faker('last_name')
    product_title = faker.bs()
    product_text = faker.bs()
    product_price = random.randint(1, 2000)