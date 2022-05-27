from django.db import models
from django.contrib.auth import get_user_model


class Snack(models.Model):
  name = models.CharField(max_length=16)
  price = models.DecimalField(decimal_places=2, max_digits=7)
  description = models.CharField(max_length=128)
  buyer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  created = models.DateField(auto_now_add=True)
  updated = models.DateField(auto_now=True)

  def __str__(self):
    return self.name

  