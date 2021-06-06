from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alert', views.AlertStockView.as_view(), name='view_user_alert'),
]