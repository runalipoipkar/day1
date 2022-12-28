from django import forms
from .models import Order
class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields='__all__'
        labels={
            'oid':'ORDER ID',
            'product_name':'PRODUCT NAME',
            'quantity':'QUANTITY',
            'del_date':'DELIVERY DATE',
            'price':'PRICE',
            'date': 'DATE',
            'address':'ADDRESS',
            'phone':'PHONE'
        }
        widgets={
            'address':forms.Textarea(),
            'del_date':forms.DateInput(
                attrs={
                    'type':'date'
                }
            )
        }