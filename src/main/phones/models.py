from django.db import models
from decimal import Decimal

class Phone(models.Model):
    model_name = models.CharField(max_length = 40)
    url = models.CharField(max_length = 150)
    price = models.DecimalField(max_digits = 12, decimal_places = 2, default = Decimal('0.00'))
    description = models.CharField(max_length = 200)

    def __str__(self):
        return self.model_name

    def __decode__(self):
        return Decimal(self.price)

