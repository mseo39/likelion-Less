from django import forms
from .models import Product, Client
from django.contrib.auth.models import User

class ClForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = '고객명'
        self.fields['content'].label = "회원정보 내용"
        self.fields['name'].widget.attrs.update({
            'class' : 'cl_name',
            'placeholder' : '제목',
        })
        self.fields['content'].widget.attrs.update({
            'class' : 'cl_content_form',
        })


class PDForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'content',)

class UserForm(forms.ModelForm):

    class Meta:
        model=User
        fields=['username','password','email']

class LoginForm(forms.ModelForm):

    class Meta:
        model=User
        fields=['username','password']