from django import forms
from .models import Comments

class commentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ["post"]
        widgets = {
            "user_comment":forms.Textarea(attrs={'placeholder': 'Write Comment','class':'form-control w-100','id':'comment','cols':'30','rows':'9'}),            
            "user_name":forms.TextInput(attrs={'placeholder': 'Name','class':'form-control','id':'name'}),
            "user_email":forms.EmailInput(attrs={'placeholder': 'Email','class':'form-control','id':'email'})
        }