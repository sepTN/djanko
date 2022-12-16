from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='kofi-index'),
    path('webhook/', views.webhook, name='kofi-webhook'),
    path('supporters/', views.supporters, name='kofi-supporters'),
    path('supporter/<int:limit>/', views.supporter, name='kofi-supporter')
]
