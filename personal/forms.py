from django import forms
from django.core.validators import RegexValidator

from personal.models import Consumer, Company


class ConsumerForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "Иванов Иван Иванович",
         'required': '',
         'autofocus': ''}),
        max_length=20,
        min_length=3,
        required=False,
        label="ФИО"
    )

    tel = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "+7 999 821 28 12",
         'required': '',
         'autofocus': ''}),
        max_length=20,
        min_length=3,
        required=False,
        label="Телефон")

    reportName = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "Сидоров Степан Валерьевич",
         'required': '',
         'autofocus': ''}),
        max_length=20,
        min_length=3,
        required=False,
        label="Название для отчётов")

    reportAddress = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "СПб, ул. Восстания, д.5",
         'required': '',
         'autofocus': ''}),
        max_length=20,
        min_length=3,
        required=False,
        label="Адрес офиса")

    reportTel = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "+7 955 89 23 23",
         'required': '',
         'autofocus': ''}),
        max_length=20,
        min_length=3,
        required=False,
        label="Телефон для обратной связи")

    reportMail = forms.EmailField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "worker@company.com",
         'required': '',
         'autofocus': 'Почта для обратной связи'}),
        max_length=20,
        min_length=3,
        required=False,
        label="Телефон")

    class Meta:
        model = Consumer
        fields = ('name', 'tel', 'reportName', 'reportAddress', 'reportTel', 'reportMail')



class CompanyForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "Логин",
         'required': '',
         'autofocus': ''}),
        max_length=20,
        min_length=3,
        required=False)

    inn = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "Логин",
         'required': '',
         'autofocus': ''}),
        max_length=20,
        min_length=3,
        required=False)

    kpp = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "Логин",
         'required': '',
         'autofocus': ''}),
        max_length=20,
        min_length=3,
        required=False)

    ogrn = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "Логин",
         'required': '',
         'autofocus': ''}),
        max_length=20,
        min_length=3,
        required=False)

    jurAddress = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "Логин",
         'required': '',
         'autofocus': ''}),
        max_length=20,
        min_length=3,
        required=False)

    fisicAddress = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "Логин",
         'required': '',
         'autofocus': ''}),
        max_length=20,
        min_length=3,
        required=False)

    rs = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "Логин",
         'required': '',
         'autofocus': ''}),
        max_length=20,
        min_length=3,
        required=False)

    bik = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "Логин",
         'required': '',
         'autofocus': ''}),
        max_length=20,
        min_length=3,
        required=False)

    b = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "Логин",
         'required': '',
         'autofocus': ''}),
        max_length=20,
        min_length=3,
        required=False)

    ks = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "Логин",
         'required': '',
         'autofocus': ''}),
        max_length=20,
        min_length=3,
        required=False)

    class Meta:
        model = Company
        fields = ('name', 'inn', 'kpp', 'ogrn', 'jurAddress', 'fisicAddress', 'rs', 'bik', 'b', 'ks')
