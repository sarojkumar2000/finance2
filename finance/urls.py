"""
URL configuration for finance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home),
    path("admin-login", views.adminLogin),
    path("user-login", views.userLogin),
    path("admin", views.admin1),
    path("user", views.user),
    path("apply-loan", views.applyloan),
    path("save", views.save),
    path("pay-due/<int:user_id>", views.pay_due),
    path("paydue/<int:user_id>", views.paydue),

]
