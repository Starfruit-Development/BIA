from django.contrib import messages
from django.core.paginator import InvalidPage
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
from oscar.core.loading import get_class, get_model

get_product_search_handler_class = get_class(
    'catalogue.search_handlers', 'get_product_search_handler_class')


from django.views.generic import ListView
from oscar.core.loading import get_model
Product = get_model('catalogue',"Product")



class HomeView(ListView):
    model = Product
    """
    Browse all products in the catalogue
    """
    context_object_name = "products"
    template_name = 'oscar/home/home.html'

    def get(self, request, *args, **kwargs):
        try:
            self.search_handler = self.get_search_handler(
                self.request.GET, request.get_full_path(), [])
            response = super().get(request, *args, **kwargs)
        except InvalidPage:
            # Redirect to page one.
            messages.error(request, _('The given page number was invalid.'))
            return redirect('catalogue:index')
        return response

    def get_queryset(self):
        return Product.objects

    def get_search_handler(self, *args, **kwargs):
        return get_product_search_handler_class()(*args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = {}
        ctx['summary'] = _("All products")
        search_context = self.search_handler.get_search_context_data(
            self.context_object_name)
        ctx.update(search_context)
        return ctx





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
