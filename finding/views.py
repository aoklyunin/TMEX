from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from finding.forms import FindingForm
from personal.models import Consumer


@login_required
# Create your views here.
def frontPage(request):
    try:
        consumer = Consumer.objects.get(user=request.user)
    except:
        messages.warning(request,
                         "Вы попытались открыть пополнение баланса, хотя сами пользователем не являетесь")
        return redirect('frontpage')

    print("ye")
    if request.method == "POST":
        finding_form = FindingForm(request.POST,request.FILES)

        if finding_form.is_valid():
            print(finding_form.cleaned_data["image"])
    else:
        finding_form = FindingForm()

    print(finding_form)

    return render(request, 'finding/front_page.html', {'form': finding_form, "balance": consumer.balance})
