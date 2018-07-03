# -*- coding: utf-8 -*-
from django.forms import ModelForm, Form
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

class UserModelForm(forms.ModelForm):
    User._meta.get_field('username').blank = False
    User._meta.get_field('first_name').blank = False
    User._meta.get_field('last_name').blank = False
    User._meta.get_field('email').blank = False
    User._meta.get_field('password').blank = False
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'maxlength': 30, 'placeholder':'Username'}),
            'first_name': forms.TextInput(attrs={'class':'form-control', 'maxlength': 30, 'placeholder':'Primeiro nome'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'maxlength': 30, 'placeholder':'Sobrenome'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'maxlength': 30, 'placeholder':'Email'}),
            'password': forms.PasswordInput(attrs={'class':'form-control', 'maxlength': 30, 'placeholder':'Senha'}),
        }

        error_messages = {
            'username':{
                'required':'Este campo é obrigatório'
            },
            'first_name':{
                'required':'Este campo é obrigatório'
            },
            'last_name':{
                'required':'Este campo é obrigatório'
            },
            'email':{
                'required':'Escreva um email válido'
            },
            'password':{
                'required':'Este campo é obrigatório'
            }
        }

    def save(self, commit=True):
        user = super(UserModelForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Usuário e/ou senha incorretos! Por favor, tente novamente!")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
