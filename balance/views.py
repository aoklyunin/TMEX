from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from balance.forms import ReplenishForm
from personal.models import Consumer
from django.contrib import messages


@login_required
# Create your views here.
def frontPage(request):
    try:
        consumer = Consumer.objects.get(user=request.user)
    except:
        messages.warning(request,
                         "Вы попытались открыть пополнение баланса, хотя сами пользователем не являетесь")
        return redirect('frontpage')

    if request.method == "POST":
        replenish_form = ReplenishForm(request.POST)

        if replenish_form.is_valid():
            consumer.balance += replenish_form.cleaned_data["value"]
            consumer.save()
    else:
        replenish_form = ReplenishForm()

    return render(request, 'balance/front_page.html', {'form': replenish_form, "balance": consumer.balance})
