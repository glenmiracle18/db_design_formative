from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CustomerViewSet, VisitViewSet, SatisfactionViewSet

router = DefaultRouter()
router.register("customers", viewset=CustomerViewSet)
router.register('visits', viewset=VisitViewSet)
router.register("satisfactions", viewset=SatisfactionViewSet)

urlpatterns = [
    path("", include(router.urls))
]