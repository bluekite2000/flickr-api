from django import forms

class WaitList(forms.Form):
	Email = forms.CharField(max_length=20)