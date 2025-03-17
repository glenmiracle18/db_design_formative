from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer


from .models import Customer, Satisfaction, Visit
from .serializers import CustomerSerializer, VisitSerializer, SatisfactionSerializer
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi





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


title = ("Formative Assignment - Database Design -Peer Group 2")

description = ("this is an api for retreiving custormer, the days and number of visit the paid to a store"
               "and the details about their satisfaction. you can go through the documentation to see how it works")

schema_view = get_schema_view(
    openapi.Info(
        title=title,
        default_version='v1',
        description=description,
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(url="https://www.github.com/danjor667"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

