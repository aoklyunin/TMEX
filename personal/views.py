from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from personal.forms import ConsumerForm
from django.contrib import messages

from personal.models import Consumer


@login_required
def frontPage(request):
    try:
        consumer = Consumer.objects.get(user=request.user)
    except:
        messages.warning(request,"Вы попытались открыть редактирование пользователя, хотя сами пользователем не являетесь")
        return redirect('frontpage')

    consumer_form = ConsumerForm(instance=consumer)

    if request.method == "POST":
        consumer_form = ConsumerForm(request.POST)

        if consumer_form.is_valid():
            consumer_form.save()
            messages.success(request,'Изменения сохранены')

    return render(request, 'personal/front_page.html', {'form': consumer_form})


# Create your views here.
def company(request):
    return render(request, 'personal/company.html')
