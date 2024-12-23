from rest_framework import serializers
from FoodApp.models import food

class ProductSerializer (serializers.ModelSerializer):
    class Meta:
        model = food
        fields = "__all__"

