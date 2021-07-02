from django.urls import path
from .views import *

urlpatterns=[
    path('new/',NewCalculationView.as_view(),name="calculation-new"),
    path('view/',ListCalculationView.as_view(),name="calculation-view"),
    path('update/<int:pk>',UpdateCalculationView.as_view(),name="calculation-update"),
    path('delete/<int:pk>',DeleteCalculationView.as_view(),name="calculation-delete"),
    path('detail/<int:pk>',DetailCalculationView.as_view(),name="calculation-detail")
]
