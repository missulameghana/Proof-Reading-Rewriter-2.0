
from django import forms

class MyForm(forms.Form):
	text_in = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "70", 'rows': "10", }),label='')
class forum(forms.Form):
	i = forms.CharField(widget=forms.HiddenInput())
	c = forms.CharField(widget=forms.HiddenInput())

