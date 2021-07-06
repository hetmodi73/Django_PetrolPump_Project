from django.urls import path
from .views import *

urlpatterns=[
    path('new/',NewNozzlleView.as_view(),name="nozzlle-new"),
    path('view/',ListNozzlleView.as_view(),name="nozzlle-view"),
    path("update/<int:pk>",UpdateNozzlleView.as_view(),name="nozzlle-update"),
    path("delete/<int:pk>",DeleteNozzlleView.as_view(),name="nozzlle-delete"),
    path("type/<int:nid>",type_of_nozzlle,name="nozzle-type"),
    path("creditor_amount/<int:nid>",get_creditor_lit_by_nozzle,name="creditor_amount")
]

