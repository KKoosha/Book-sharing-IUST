from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length = 100)
    email = forms.EmailField(required = False)
    message = forms.CharField(widget=forms.Textarea)

class UploadForm(forms.Form):
    name=forms.CharField(max_length = 100)
    author=forms.CharField(max_length = 100)
    comment=forms.CharField(max_length = 300)
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )


    