from django import forms
from .models import Duty, Order

class DutyForm(forms.ModelForm):
    class Meta:
        model = Duty
        fields=['name','department','hours']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product']