from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm, UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import fields, widgets
from django.utils.translation import gettext,gettext_lazy as _
from .models import Customer, Product

class CustomerRegisterForm(UserCreationForm):
    password1= forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'from-control'}))
    password2= forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'from-control'}))
    email= forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'from-control'}))

    class Meta:
        model=User
        fields=['username','email','password1','password2']
        labels={'email':'Email'}
        widgets= {'username':forms.TextInput(attrs={'class':'form-control'})}



#Authentication Form Start Here

class LoginForm(AuthenticationForm):
    username= UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'from-control'}))
    password= forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'from-control'}))


class MyPschangeForm(PasswordChangeForm):
    old_password= forms.CharField(label=_("Old Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True, 'class':'from-control'}))
    new_password1= forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'from-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2= forms.CharField(label=_("Confirm New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'from-control'}))


class MyPasswordResetForm(PasswordResetForm):
    email=forms.EmailField(label=_("Email"),max_length=254,widget=forms.EmailInput(attrs={'autocomplete':'email', 'class':'from-control'}))

    

class MySetPasswordForm(SetPasswordForm):
    new_password1= forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'from-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2= forms.CharField(label=_("Confirm New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'from-control'}))




class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','locality','city','state','zipcode']
        widgets= {'name':forms.TextInput(attrs={'class':'form-control'}),
        'locality':forms.TextInput(attrs={'class':'form-control'}),
        'city':forms.TextInput(attrs={'class':'form-control'}),
        'state':forms.Select(attrs={'class':'form-control'}),
        'zipcode':forms.NumberInput(attrs={'class':'form-control'})
        }

class AddItemForm(forms.ModelForm):
    class Meta:
        model= Product
        fields= ('title','description','brand','category','selling_price','discounted_price','product_image')

        widgets={
            'title':forms.TextInput(attrs={'class': 'form-control'  }),
            'description':forms.Textarea(attrs={'class': 'form-control'  }),
            'brand':forms.TextInput(attrs={'class': 'form-control'  }),
            'selling_price':forms.TextInput(attrs={'class': 'form-control'  }),
            'category':forms.Select(attrs={'class': 'form-control'  }),
            #'product_image':forms.ImageField(attrs={'class': 'form-control'  }),
            'discounted_price':forms.TextInput(attrs={'class':'form-control'}),
        }