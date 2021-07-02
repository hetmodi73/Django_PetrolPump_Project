from django.urls import path
from .views import *

urlpatterns=[
    path('new/',NewNozzlle_tView.as_view(),name="nozzlle_transaction-new"),
    path('view/',ListNozzlle_tView.as_view(),name="nozzlle_transaction-view"),
    path('update/<int:pk>',UpdateNozzlle_tView.as_view(),name="nozzlle_transaction-update"),
    path('delete/<int:pk>',DeleteNozzlle_tView.as_view(),name="nozzlle_transaction-delete"),
    path('detail/<int:pk>',DetailNozzlle_tView.as_view(),name="nozzlle_transaction-detail")
]
