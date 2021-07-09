from django.urls import path
from .views import *

urlpatterns=[
    path('new/',NewExpenseView.as_view(),name="expense_detail-new"),
    path('view/',ListExpenseView.as_view(),name="expense_detail-view"),
    path('update/<int:pk>',UpdateExpenseView.as_view(),name="expense_detail-update"),
    path('delete/<int:pk>',DeleteExpenseView.as_view(),name="expense_detail-delete"),
    path('detail/<int:pk>',DetailExpenseView.as_view(),name="expense_detail-detail")
]
