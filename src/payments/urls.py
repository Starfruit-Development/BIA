from django.urls import path

from . import views

urlpatterns = [
    path('payments/config/', views.stripe_config),
    path('payments/create-checkout-session/', views.create_checkout_session), # new
]