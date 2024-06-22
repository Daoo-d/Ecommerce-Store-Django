from django import forms
from .models import PlaceOrder

class ShippingForm(forms.ModelForm):
    class Meta:
        model = PlaceOrder
        exclude = ["customer","order","date_added"]
        widgets = {
            "address":forms.TextInput(attrs={'placeholder': 'Address','class':'form-control'}),
            "city":forms.TextInput(attrs={'placeholder': 'City','class':'form-control'}),
            "state":forms.TextInput(attrs={'placeholder': 'State/Province','class':'form-control'}),
            "contact":forms.TextInput(attrs={'placeholder': 'Contact Number','class':'form-control'})
        }