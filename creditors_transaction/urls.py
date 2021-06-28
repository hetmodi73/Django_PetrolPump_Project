from django.urls import path
from .views import *

urlpatterns=[
    path('new/',NewCreditor_transactionView.as_view(),name="creditor_transaction-new"),
    path('view/',ListCreditor_transactionView.as_view(),name="creditor_transaction-view"),
    path('update/<int:pk>',UpdateCreditor_transactionView.as_view(),name="creditor_transaction-update"),
    path('delete/<int:pk>',DeleteCreditor_transactionView.as_view(),name="creditor_transaction-delete"),
    path('detail/<int:pk>',DetailCreditor_transactionView.as_view(),name="creditor_transaction-detail")
]
