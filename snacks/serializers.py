from rest_framework import serializers
from .models import Snack


class SnackSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'name', 'price', 'description', 'buyer', 'created')
    model = Snack
