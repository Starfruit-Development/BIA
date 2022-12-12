from django import forms

class OrderSearchForm(forms.Form):
    order_number = forms.CharField(required=False, label =("Número del pedido"))
    email = forms.EmailField(label=('Email'))

    '''def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)'''