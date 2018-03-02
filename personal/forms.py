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
        max_length=80,
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
        max_length=80,
        min_length=3,
        required=False,
        label="Телефон")

    reportName = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "Сидоров Степан Валерьевич",
         'required': '',
         'autofocus': ''}),
        max_length=80,
        min_length=3,
        required=False,
        label="Название для отчётов")

    reportAddress = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "СПб, ул. Восстания, д.5",
         'required': '',
         'autofocus': ''}),
        max_length=80,
        min_length=3,
        required=False,
        label="Адрес офиса")

    reportTel = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "+7 955 89 23 23",
         'required': '',
         'autofocus': ''}),
        max_length=80,
        min_length=3,
        required=False,
        label="Телефон для обратной связи")

    reportMail = forms.EmailField(widget=forms.EmailInput(
        attrs=
        {'class': "form-control",
         'placeholder': "worker@company.com",
         'required': '',
         'autofocus': ''}),
        max_length=80,
        min_length=3,
        required=False,
        label="Почта для обратной связи")

    class Meta:
        model = Consumer
        fields = ('name', 'tel', 'reportName', 'reportAddress', 'reportTel', 'reportMail')



class CompanyForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "ПАО газпром",
         'required': '',
         'autofocus': ''}),
        max_length=80,
        min_length=3,
        label="Название",
        required=False)

    inn = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': '7826655214',
         'required': '',
         'autofocus': ''}),
        max_length=10,
        min_length=10,
        label="ИНН",
        required=False)

    kpp = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "781951012",
         'required': '',
         'autofocus': ''}),
        max_length=9,
        min_length=9,
        label="КПП",
        required=False)

    ogrn = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "1027810987398",
         'required': '',
         'autofocus': ''}),
        max_length=13,
        min_length=10,
        label="ОРГН",
        required=False)

    jurAddress = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "г. Спб, Литейный пр., д.5, оф. 19",
         'required': '',
         'autofocus': ''}),
        max_length=80,
        label="Юридический адрес",
        min_length=3,
        required=False)

    fisicAddress = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "п. Шушары, Пушкинская ул., д.22, оф. 251",
         'required': '',
         'autofocus': ''}),
        max_length=80,
        label="Физический адрес",
        min_length=3,
        required=False)

    rs = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "40703450955265465464",
         'required': '',
         'autofocus': ''}),
        max_length=22,
        label="Р/С",
        min_length=18,
        required=False)

    bik = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "044230613",
         'required': '',
         'autofocus': ''}),
        max_length=9,
        min_length=9,
        label="БИК",
        required=False)

    b = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "Северо-Западный Банк ОАО «Сбербанк России»",
         'required': '',
         'autofocus': ''}),
        max_length=80,
        min_length=3,
        label="Банк",
        required=False)

    ks = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "30103432500000000653",
         'required': '',
         'autofocus': ''}),
        max_length=22,
        label="К/С",
        min_length=18,
        required=False)

    class Meta:
        model = Company
        fields = ('name', 'inn', 'kpp', 'ogrn', 'jurAddress', 'fisicAddress', 'rs', 'bik', 'b', 'ks')
