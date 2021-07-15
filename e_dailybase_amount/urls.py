from django.urls import path
from .views import *

urlpatterns=[
    path('new/',NewDailybase_aView.as_view(),name="e_dailybase_amount-new"),
    path('view/',ListDailybase_aView.as_view(),name="e_dailybase_amount-view"),
    path('update/<int:pk>',UpdateDailybase_aView.as_view(),name="e_dailybase_amount-update"),
    path('delete/<int:pk>',DeleteDailybase_aView.as_view(),name="e_dailybase_amount-delete"),
    path('detail/<int:pk>',DetailDailybase_aView.as_view(),name="e_dailybase_amount-detail")
]
