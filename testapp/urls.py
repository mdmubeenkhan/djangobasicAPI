from django.urls import path, include
from rest_framework.routers import DefaultRouter
from testapp.views import EmployeeView, EmployeeAPIView

router = DefaultRouter()
router.register('api', EmployeeView, basename='apis')

urlpatterns = [
    path('', include(router.urls)),
    path('apiview/', EmployeeAPIView.as_view()),
]