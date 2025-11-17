from django.urls import path
from .views import CarListApiView, CarCreateApiView, CarEditApiView, CarDeleteApiView

urlpatterns = [
    path('cars/', CarListApiView.as_view(), name='cars_view'),
    path('cars/create/', CarCreateApiView.as_view(), name='cars_create'),
    path('cars/edit/<int:pk>/', CarEditApiView.as_view(), name='cars_edit'),
    path('cars/delete/<int:pk>/', CarDeleteApiView.as_view(), name='cars_delete')
]