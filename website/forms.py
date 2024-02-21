from django import forms
from website.models import Contact,newslettr
from captcha.fields import CaptchaField


class Nameform(forms.Form):
    name=forms.CharField(max_length=255)
    email=forms.EmailField()
    subject = forms.CharField(max_length=255, required=False)
    message=forms.CharField(widget=forms.Textarea)
    

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields=  '__all__' 

class newslettr(forms.ModelForm):

    class Meta():
        model = newslettr
        fields= '__all__'