from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
import sys
sys.path.append("..")
from products.models import Product

User = get_user_model()


class Order(models.Model):
    quantity = models.IntegerField(null=False, blank=False, default=1)
    order_time = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
