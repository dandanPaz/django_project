from rest_framework import serializers
from .models import Product,Customers




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'
    def create(self, validated_data):
        user = self.context['user']
        print(user)
        return Customers.objects.create(**validated_data,user=user)


