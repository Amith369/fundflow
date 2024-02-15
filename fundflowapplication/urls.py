"""
URL configuration for fundflowapplication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from budget import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("transaction/all/",views.TransactionListView.as_view(),name="transaction-list"),
    path("transaction/add/",views.TransactionCreateView.as_view(),name="transaction-add"),
    path("transaction/<int:pk>/",views.TransactionDetailView.as_view(),name="transaction_detail"),
    path("transaction/<int:pk>/remove/",views.TransactionDeleteView.as_view(),name="transaction-remove"),
    path("transaction/<int:pk>/change/",views.TransactionUpdateView.as_view(),name="transaction-change"),
    path("signup/",views.SignUpView.as_view(),name="signup"),
    path("",views.SignInView.as_view(),name="signin"),
    path("signout/",views.SignOutView.as_view(),name="signout"),

    
]
