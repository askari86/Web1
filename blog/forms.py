from django import forms
from blog.models import comment
from captcha.fields import CaptchaField

class CommentForm(forms.ModelForm):
    # captcha = CaptchaField()

    class Meta:
        model = comment
        fields=  ['name', 'email', 'subject', 'message' , 'post'] 