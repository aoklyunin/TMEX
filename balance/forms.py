from django import forms



class ReplenishForm(forms.Form):

    value = forms.FloatField(widget=forms.TextInput(
        attrs=
        {'class': "form-control pageInput",
         'placeholder': "100.0",
         'required': '',
         'autofocus': ''}),
        label="Сумма",
        required=True,)
