from django.urls import path, include
from rest_framework.routers import DefaultRouter
from testapp.views import EmployeeView

router = DefaultRouter()
router.register('api', EmployeeView, basename='apis')

urlpatterns = [
    path('', include(router.urls)),
]