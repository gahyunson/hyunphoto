from django import forms


class ContactForm(forms.Form):
    message = forms.CharField(label='message', max_length=1024, 
                              widget=forms.Textarea(attrs={'placeholder': 'Write your message.'})
                              )