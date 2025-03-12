from rest_framework import serializers

from .models import Customer, Visit, Satisfaction


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'
        extra_kwargs = {
            'customer_id': {'read_only': True}
        }


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'




class SatisfactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Satisfaction
        fields = '__all__'


