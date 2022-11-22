from subscribers import views
from django.urls import re_path

app_name = 'subscribers'

urlpatterns = [
    re_path(r'^subscribe/', views.subscribe_by_email, name='email_subscription'),
]
