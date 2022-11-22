from django.urls import re_path
from django.urls.conf import include, path

from cart import views

app_name = 'cart'


apipatterns = [

]

urlpatterns = [
    re_path(r'^add-to-cart$', views.add_to_cart, name='add'),
    re_path(r'^payment/process$', views.ProcessPaymentView.as_view(), name='pay'),
    re_path(r'^coupon-add$', views.apply_coupon, name='add_coupon'),
    re_path(r'^alter/(?P<pk>\d+)/(?P<method>(add|reduce))$', views.alter_item_quantity, name='alter_quantity'),
    re_path(r'^(?P<pk>\d+)/delete$', views.delete_product_from_cart, name='delete'),

    re_path(r'^shipment$', views.ShipmentView.as_view(), name='shipment'),
    re_path(r'^payment$', views.PaymentView.as_view(), name='payment'),
    re_path(r'^success$', views.CartSuccessView.as_view(), name='success'),
    re_path(r'^no-cart$', views.EmptyCartView.as_view(), name='no_cart'),
    re_path(r'^$', views.CheckoutView.as_view(), name='checkout'),
]
