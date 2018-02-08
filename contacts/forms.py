# -*- coding: utf-8 -*-
from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	sender = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	message = forms.CharField(widget = forms.Textarea(attrs = {'class': 'form-control'}))
	