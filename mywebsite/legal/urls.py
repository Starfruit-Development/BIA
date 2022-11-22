from django.urls import re_path
from django.views.generic import TemplateView

from legal import views

app_name = 'legal'

urlpatterns = [
    re_path(r'^who-we-are$', views.AboutView.as_view(), name='who_we_are'),
    re_path(r'^terms-of-service$', views.CGU.as_view(), name='use'),
    re_path(r'^terms-of-sale$', views.CGV.as_view(), name='sale'),
    re_path(r'^privacy$', views.Confidentialite.as_view(), name='privacy'),
]
