from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from personal.forms import ConsumerForm, CompanyForm
from django.contrib import messages

from personal.models import Consumer, Company


@login_required
def frontPage(request):
    try:
        consumer = Consumer.objects.get(user=request.user)
    except:
        messages.warning(request,
                         "Вы попытались открыть редактирование пользователя, хотя сами пользователем не являетесь")
        return redirect('frontpage')

    if request.method == "POST":
        consumer_form = ConsumerForm(request.POST)

        if consumer_form.is_valid():
            Consumer.objects.filter(user=request.user).update(**consumer_form.cleaned_data)
            messages.success(request, 'Изменения сохранены')
    else:
        consumer_form = ConsumerForm(instance=consumer)

    return render(request, 'personal/front_page.html', {'form': consumer_form})


# Create your views here.
def company(request):
    try:
        consumer = Consumer.objects.get(user=request.user)
    except:
        messages.warning(request,
                         "Вы попытались открыть редактирование компании, хотя сами пользователем не являетесь")
        return redirect('frontpage')

    company = consumer.companies.first()
    if company is None:
        company = Company.objects.create()
        consumer.companies.add(company)

    print(company.pk)

    if request.method == "POST":
        company_form = CompanyForm(request.POST)

        if company_form.is_valid():
            Company.objects.filter(pk=company.pk).update(**company_form.cleaned_data)
            messages.success(request, 'Изменения сохранены')
    else:
        company_form = CompanyForm(instance=company)

    return render(request, 'personal/company.html', {'form': company_form})
