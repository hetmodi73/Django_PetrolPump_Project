from django.urls import path
from .views import *

urlpatterns=[
    path('new/',NewEmployeeView.as_view(),name="employee-new"),
    path('view/',ListEmployeeView.as_view(),name="employee-view"),
    path("update/<int:pk>",UpdateEmployeeView.as_view(),name="employee-update"),
    path("delete/<int:pk>",DeleteEmployeeView.as_view(),name="employee-delete"),
    path("detail/<int:pk>",DetailEmployeeView.as_view(),name="employee-detail")
]
