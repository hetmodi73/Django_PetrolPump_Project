"""Django_PetrolPump_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from client.views import home
from django.contrib.auth.views import LoginView,LogoutView
from django .conf import settings
from django .conf.urls.static import static
from client.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',home,name="home-page"),
    path("",LoginView.as_view(template_name='client/login.html'),name="login"),
    path("logout",LogoutView.as_view(template_name='client/logout.html'),name='logout'),
    path("rates/",include("rates.urls")),
    path("nozzlle_master/",include("nozzlle_master.urls")),
    path("employee_master/",include("employee_master.urls")),
    path("tank_master/",include("tank_master.urls")),
    path("creditors_master/",include("creditors_master.urls")),
    path("vehicle_master/",include("vehicle_master.urls")),
    path("creditors_transaction/",include("creditors_transaction.urls")),
    path("creditors_payment/",include("creditors_payment.urls")),
    path("suppliers_master/",include("suppliers_master.urls")),
    path("employee_payment/",include("employee_payment.urls")),
    path("nozzlle_transaction/",include("nozzlle_transaction.urls")),
    path("calculation_master/",include("calculation_master.urls")),
    path("dashboard/",dashboard,name="dashboard")
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
