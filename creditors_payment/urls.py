from django.urls import path
from .views import *

urlpatterns=[
    path('new/',NewPaymentView.as_view(),name="creditors_payment-new"),
    path('view/',ListPaymentView.as_view(),name="creditors_payment-view"),
    path('update/<int:pk>',UpdatePaymentView.as_view(),name="creditors_payment-update"),
    path('delete/<int:pk>',DeletePaymentView.as_view(),name="creditors_payment-delete"),
    path('detail/<int:pk>',DetailPaymentView.as_view(),name="creditors_payment-detail")
]
