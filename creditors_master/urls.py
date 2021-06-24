from django.urls import path
from .views import *

urlpatterns=[
    path('new/',NewCreditorsView.as_view(),name="tank-new"),
    path('view/',ListCreditorsView.as_view(),name="tank-view"),
    path('update/<int:pk>',UpdateCreditorsView.as_view(),name="tank-update"),
    path('delete/<int:pk>',DeleteCreditorsView.as_view(),name="tank-delete"),
    path('detail/<int:pk>',DetailCreditorsView.as_view(),name="tank-detail"),
]
