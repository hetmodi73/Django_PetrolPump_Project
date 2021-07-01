from django.urls import path
from .views import *

urlpatterns=[
    path('new/',NewSuppliersView.as_view(),name="suppliers_master-new"),
    path('view/',ListSuppliersView.as_view(),name="suppliers_master-view"),
    path('update/<int:pk>',UpdateSuppliersView.as_view(),name="suppliers_master-update"),
    path('delete/<int:pk>',DeleteSuppliersView.as_view(),name="suppliers_master-delete"),
    path('detail/<int:pk>',DetailSuppliersView.as_view(),name="suppliers_master-detail")
]
