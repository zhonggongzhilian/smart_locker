# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "用户名",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "密码",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "用户名",
                "class": "form-control"
            }
        ))

    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "手机号",
                "class": "form-control"
            }
        ),
        validators=[
            # 你可以在这里添加手机号格式的验证
            # 例如：RegexValidator(r'^\d{11}$', '手机号格式不正确')
        ]
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "密码",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "再次输入密码",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'password1', 'password2')
