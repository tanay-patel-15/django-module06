from django.urls import path
from . import views

urlpatterns = [
  path("", views.Inputs),
  path('trial', views.Trial),
  path("payroll", views.Payroll)
]