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
    customer = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all())

    class Meta:
        model = Visit
        fields = '__all__'
        extra_kwargs = {
            'visit_id': {'read_only': True}
        }




class SatisfactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Satisfaction
        fields = '__all__'
        extra_kwargs = {
            'satisfaction_id': {'read_only': True}
        }


