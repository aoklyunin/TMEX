from django import forms



class FindingForm(forms.Form):
    image = forms.ImageField(widget=forms.FileInput(attrs={'required': True, 'class': 'form-control', 'enctype': 'multipart/form-data'}))

