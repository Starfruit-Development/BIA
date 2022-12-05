from django.contrib import messages
from django.core.paginator import InvalidPage
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView, FormView
from oscar.core.loading import get_class, get_model
from django.views import generic
from django.shortcuts import get_object_or_404
from django import http
Order = get_model('order', 'Order')
OrderSearchForm = get_class('home.models', 'OrderSearchForm')

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




class OrderSearchView(FormView):
    model = Order
    template_name = "oscar/home/anon_order_form.html"
    success_url = reverse_lazy('customer:profile-view')
    form_class = OrderSearchForm
    
    def get_object(self, queryset=None):
        orderToShow = Order.objects.get(number = self.kwargs['order_number'])
    
        email = self.kwargs['guest_email']
        order = get_object_or_404(self.model, user=None,
                                  number=self.kwargs['order_number'])

        if not getattr(order,"guest_email") == email:
            raise http.Http404()
        return orderToShow

    def form_valid(self, form):

        order = get_object_or_404(Order, user=None,
                                  number=form.data['order_number'])
    
        return redirect(reverse_lazy('customer:anon-order',
                        kwargs = {
                            "order_number": getattr(order,"number"),
                            "hash": order.verification_hash()
                        }
         ))