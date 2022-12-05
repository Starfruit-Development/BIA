from django.apps import apps
from django.urls import include, path, re_path
from django.utils.translation import gettext_lazy as _

from oscar.core.loading import get_class
from oscar.core.application import OscarConfig


class HomeConfig(OscarConfig):
    label = 'home'
    name = 'oscar.apps.home'
    verbose_name = _('Home')

    namespace = 'home'

    def ready(self):
        super().ready()

        self.home_view = get_class('home.views', 'HomeView')
        self.termsOfUse_view = get_class('home.views', 'TermsOfUseView')
        self.about_us_view = get_class('home.views', 'AboutUsView')
        self.order_search_view = get_class('home.views', 'OrderSearchView')


    def get_urls(self):
        urls = super().get_urls()
        urls += [
            path('home', self.home_view.as_view(), name='index'),
            path('aboutUs', self.about_us_view.as_view(), name='aboutUs'),
            path('termsOfUse', self.termsOfUse_view.as_view(), name='termsOfUse'),
            path('searchOrder',self.order_search_view.as_view(), name="searchOrder")
        ]
        return self.post_process_urls(urls)