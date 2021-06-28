from django.urls import path
from .views import *

urlpatterns=[
    path('new/',NewVehicleView.as_view(),name="vehicle-new"),
    path('view/',ListVehicleView.as_view(),name="vehicle-view"),
    path('update/<int:pk>',UpdateVehicleView.as_view(),name="vehicle-update"),
    path('delete/<int:pk>',DeleteVehicleView.as_view(),name="vehicle-delete"),
    path('detail/<int:pk>',DetailVehicleView.as_view(),name="vehicle-detail")
]
