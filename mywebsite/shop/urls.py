from django.urls import include, path, re_path

from shop import views

app_name='shop'

urlpatterns = [
    re_path(r'^(?P<pk>\d+)/add-like$', views.add_like, name='like'),
    re_path(r'^(?P<pk>\d+)/add-review$', views.add_review, name='new_review'),

    re_path(r'^size-guide/calculate$', views.size_calculator, name='calculator'),
    re_path(r'^size-guide$', views.SizeGuideView.as_view(), name='size_guide'),
    re_path(r'^search$', views.SearchView.as_view(), name='search'),

    re_path(r'^private/(?P<pk>\d+)/(?P<slug>[a-z\-]+)$', views.PrivateProductView.as_view(), name='private'),
    re_path(r'^preview/(?P<pk>\d+)/(?P<slug>[a-z\-]+)$', views.PreviewProductView.as_view(), name='preview'),
    
    re_path(r'^collections/(?P<gender>(women|men))/(?P<collection>[a-z]+)/(?P<pk>\d+)/(?P<slug>[a-z0-9\-]+)$', views.ProductView.as_view(), name='product'),
    re_path(r'^collections/(?P<gender>(women|men))/(?P<collection>[a-z]+)$', views.ProductsView.as_view(), name='collection'),
    re_path(r'^collections/(?P<gender>(women|men))$', views.ShopGenderView.as_view(), name='gender'),

    re_path(r'^$', views.IndexView.as_view(), name='home')
]
