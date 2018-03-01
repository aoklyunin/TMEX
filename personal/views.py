from django.shortcuts import render

# Create your views here.
def frontPage(request):
    return render(request, 'public/front_page.html')

# Create your views here.
def company(request):
    return render(request, 'public/front_page.html')
