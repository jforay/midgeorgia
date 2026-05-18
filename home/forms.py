from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20, required=False)
    question = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), label='Message / Question')
