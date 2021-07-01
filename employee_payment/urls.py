from django.urls import path
from .views import *

urlpatterns=[
    path('new/',NewEmployeeView.as_view(),name="employee_payment-new"),
    path('view/',ListEmployeeView.as_view(),name="employee_payment-view"),
    path('update/<int:pk>',UpdateEmployeeView.as_view(),name="employee_payment-update"),
    path('delete/<int:pk>',DeleteEmployeeView.as_view(),name="employee_payment-delete"),
    path('detail/<int:pk>',DetailEmployeeView.as_view(),name="employee_payment-detail")
]
