from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

import stripe

class HomePageView(TemplateView):
    template_name = 'payments.html'

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    item_list = create_item_list(request)
        
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - capture the payment later
            # [customer_email] - prefill the email input in the form
            # For full details see https://stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'es/checkout/preview/',
                cancel_url=domain_url,
                payment_method_types=['card'],
                mode='payment',
                line_items=item_list
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})

def get_prices_and_products():
    product_list = stripe.Product.list(limit=100, active = True)['data']
    price_list = stripe.Price.list(limit=100)['data']

    flag = True
    while flag:
        if len(product_list) % 100 == 0:
            product_list += stripe.Product.list(limit=100, starting_after=product_list[-1], active = True)['data']
        else:
            flag = False

    flag = True
    while flag:
        if len(price_list) % 100 == 0:
            price_list += stripe.Price.list(limit=100, starting_after=price_list[-1])['data']
        else:
            flag = False

    return [product_list, price_list]

def create_item_list(request):
    item_list = []
    product_list, price_list = get_prices_and_products()

    for line in request.basket.all_lines():
        for product in product_list:
            if product.name == line.product.get_title():
                for price in price_list:
                    if price.product == product.id: 
                        item_list.append({
                            'price': price.id,
                            'quantity': line.quantity
                        })

    return item_list