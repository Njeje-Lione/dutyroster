from django import forms
from .models import Duty, Order, Leave, Complains, Ward

class DutyForm(forms.ModelForm):
    class Meta:
        model = Duty
        fields=['name','department','hours','shift','ward']

class WardForm(forms.ModelForm):
    class Meta:
        model= Ward
        fields = ['name','department','floor','building']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product','activity']

class Leaveform(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ['name','email','department']

class ComplainForm(forms.ModelForm):
    class Meta:
        model = Complains
        fields =  ['name','email','department','type','brief_description']