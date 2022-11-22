from django.urls import re_path

from store import views

app_name = 'store'

urlpatterns = [
    re_path(r'^(?P<pk>\d+)/(?P<product>\d+)/(?P<slug>[a-z\-]+)$', views.StoreProductDetailView.as_view(), name='product'),
    re_path(r'^(?P<pk>\d+)$', views.StoreView.as_view(), name='products'),
    re_path(r'^$',views.StoresView.as_view(), name='home'),
]
