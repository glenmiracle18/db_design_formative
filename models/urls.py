from django.urls import include, path
from rest_framework.routers import DefaultRouter

from models import views
from models.views import CustomerViewSet, VisitViewSet, SatisfactionViewSet

router = DefaultRouter()
router.register("customers", viewset=CustomerViewSet)
router.register('visits', viewset=VisitViewSet)
router.register("satisfactions", viewset=SatisfactionViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path('api/', include(router.urls))
]