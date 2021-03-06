from django.urls import path

# from .models import print_page
from .views import *

urlpatterns=[
    path('new/',NewCreditorsView.as_view(),name="creditors-new"),
    path('view/',ListCreditorsView.as_view(),name="creditors-view"),
    path('update/<int:pk>',UpdateCreditorsView.as_view(),name="creditors-update"),
    path('delete/<int:pk>',DeleteCreditorsView.as_view(),name="creditors-delete"),
    path('detail/<int:pk>',DetailCreditorsView.as_view(),name="creditors-detail"),
    # path("print/<int:id>",print_page,name="print-page")
]
