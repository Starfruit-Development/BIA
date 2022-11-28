from urllib.parse import quote

from django.contrib import messages
from django.core.paginator import InvalidPage
from django.http import Http404, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, TemplateView

from oscar.apps.catalogue.signals import product_viewed
from oscar.core.loading import get_class, get_model

get_product_search_handler_class = get_class(
    'catalogue.search_handlers', 'get_product_search_handler_class')


class HomeView(TemplateView):
    """
    Browse all products in the catalogue
    """
    
    template_name = 'oscar/home/home.html'

    def get(self, request, *args, **kwargs):
        try:
            self.search_handler = self.get_search_handler(
                self.request.GET, request.get_full_path(), [])
            response = super().get(request, *args, **kwargs)
        except InvalidPage:
            # Redirect to page one.
            messages.error(request, _('The given page number was invalid.'))
            # return redirect('catalogue:index')
        return response
        
        
    def get_search_handler(self, *args, **kwargs):
        return get_product_search_handler_class()(*args, **kwargs)

    '''
    def get_context_data(self, **kwargs):
        ctx = {}
        ctx['summary'] = _("Escaparate")
        search_context = self.search_handler.get_search_context_data(
            self.context_object_name)
        ctx.update(search_context)
        return ctx
    '''

class AboutUsView(TemplateView):
    
    template_name = 'oscar/home/aboutUs.html'
    
    def get(self, request, *args, **kwargs):
        try:
            self.search_handler = self.get_search_handler(
                self.request.GET, request.get_full_path(), [])
            response = super().get(request, *args, **kwargs)
        except InvalidPage:
            # Redirect to page one.
            messages.error(request, _('The given page number was invalid.'))
            # return redirect('catalogue:index')
        return response
    
    def get_search_handler(self, *args, **kwargs):
        return get_product_search_handler_class()(*args, **kwargs)    

class TermsOfUseView(TemplateView):
    template_name = 'oscar/home/termsOfUse.html'

    def get(self, request, *args, **kwargs):
        try:
            self.search_handler = self.get_search_handler(
                self.request.GET, request.get_full_path(), [])
            response = super().get(request, *args, **kwargs)
        except InvalidPage:
            # Redirect to page one.
            messages.error(request, _('The given page number was invalid.'))
            # return redirect('catalogue:index')
        return response
    
    def get_search_handler(self, *args, **kwargs):
        return get_product_search_handler_class()(*args, **kwargs)
