from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response

from models.models import Customer, Satisfaction, Visit
from models.serializers import CustomerSerializer, VisitSerializer, SatisfactionSerializer


@api_view(['GET'])
def index(request):
    return Response({"message": "Hello, world!"})


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]



class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]



class SatisfactionViewSet(viewsets.ModelViewSet):
    queryset = Satisfaction.objects.all()
    serializer_class = SatisfactionSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

