from django.urls import path
from .views import *

urlpatterns=[
    path('new/',NewEmployee_pView.as_view(),name="employee_payment-new"),
    path('view/',ListEmployee_pView.as_view(),name="employee_payment-view"),
    path('update/<int:pk>',UpdateEmployee_pView.as_view(),name="employee_payment-update"),
    path('delete/<int:pk>',DeleteEmployee_pView.as_view(),name="employee_payment-delete"),
    path('detail/<int:pk>',DetailEmployee_pView.as_view(),name="employee_payment-detail")
]
