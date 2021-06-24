from django.urls import path
from .views import *

urlpatterns=[
    path('new/',NewTankView.as_view(),name="tank-new"),
    path('view/',ListTankView.as_view(),name="tank-view"),
    path('update/<int:pk>',UpdateTankView.as_view(),name="tank-update"),
    path('delete/<int:pk>',DeleteTankView.as_view(),name="tank-delete"),
    path('detail/<int:pk>',DetailTankView.as_view(),name="tank-detail"),
    path("petrolprice/",petrol_same_date_rate,name="petrol-price"),
    path("dieselprice/",diesel_same_date_rate,name="diesel-price")
]
