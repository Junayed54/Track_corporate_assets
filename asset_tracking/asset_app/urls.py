from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserAPIView, CompanyListCreateView, CompanyRetrieveUpdateDestroyView,
    DeviceListCreateView, DeviceRetrieveUpdateDestroyView, DeviceAssignView,
    EmployeeListCreateView, EmployeeRetrieveUpdateDestroyView, EmployeeAssignmentsListView,
    DeviceAssignmentViewSet
)


router = DefaultRouter()
router.register(r'device-assignments', DeviceAssignmentViewSet, basename='device-assignment')

urlpatterns = [
    path('user/', UserAPIView.as_view(), name='user-detail'),

    path('companies/', CompanyListCreateView.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyRetrieveUpdateDestroyView.as_view(), name='company-detail'),
    path('devices/', DeviceListCreateView.as_view(), name='device-list'),
    path('devices/<int:pk>/', DeviceRetrieveUpdateDestroyView.as_view(), name='device-detail'),
    path('devices/<int:pk>/assign/', DeviceAssignView.as_view(), name='device-assign'),
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-detail'),
    path('employees/<int:pk>/assignments/', EmployeeAssignmentsListView.as_view(), name='employee-assignments'),
    path('', include(router.urls)),
]
