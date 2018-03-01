# -*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse, HttpResponseBadRequest, Http404, \
    HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.template import RequestContext
from django.contrib.auth import logout, login, authenticate

from personal.models import Consumer
from tmex.forms import ConsumerForm
from tmex.utils.helpers import post_only


def permissionDenied(request):
    return render(request, 'permissionDenied.html', {})


def about(request):
    return render(request, 'public/about.html', {})


def start(request):
    return render(request, 'public/start.html', {})


def attorney(request):
    return render(request, 'public/attorney.html', {})


def help(request):
    return render(request, 'public/help.html', {})


def price(request):
    return render(request, 'public/price.html', {})


def restore(request):
    return render(request, 'public/restore.html', {})


def frontPage(request):
    return render(request, 'public/front_page.html')


def ehandler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def ehandler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response


@post_only
def signin(request):
    """
    Pretty straighforward user authentication using password and username
    supplied in the POST request.
    """

    print(request.POST)

    redirect_page = request.POST.get('redirect_path', '/')

    if request.user.is_authenticated():
        messages.warning(request, "Вы уже вошли")
        return redirect(redirect_page)

    username = request.POST.get('username')
    password = request.POST.get('password')

    if not username or not password:
        return HttpResponseBadRequest()

    user = authenticate(username=username,
                        password=password)

    if user:
        if user.is_active:
            login(request, user)
            return redirect(redirect_page)
        else:
            messages.error("Доступ запрещён")
            return HttpResponseBadRequest()
    else:
        messages.error("Пара логин/пароль не найдена")
        return HttpResponseBadRequest()


def signout(request):
    """
    Log out user if one is logged in and redirect them to frontpage.
    """

    if request.user.is_authenticated():
        redirect_page = request.POST.get('current_page', '/')
        logout(request)
        messages.success(request, 'Вы вышли')
        return redirect(redirect_page)

    return redirect('frontpage')


def signup(request):
    """
    Handles user registration using UserForm from forms.py
    Creates new User and new RedditUser models if appropriate data
    has been supplied.

    If account has been created user is redirected to login page.
    """
    user_form = ConsumerForm()
    if request.user.is_authenticated():
        messages.warning(request, 'Вы уже зарегистрированы и вошли')
        return render(request, 'public/signup.html', {'form': user_form})

    if request.method == "POST":
        user_form = ConsumerForm(request.POST)

        if user_form.is_valid():
            if user_form.cleaned_data["password"] != user_form.cleaned_data["rep_password"]:
                messages.error(request, 'пароли не совпадают')
            else:
                username = user_form["username"]
                try:
                    User.objects.get(username=username)
                    messages.error(request, 'пользователь уже существует')
                except (User.DoesNotExist):
                    new_user = User(username=username)
                    new_user.set_password(user_form.cleaned_data["password"])
                    new_user.save()
                    consumer = Consumer()
                    consumer.user = new_user
                    consumer.save()
                    user = authenticate(username=request.POST['username'],
                                        password=request.POST['password'])
                    login(request, user)
                return redirect('frontpage')

    return render(request, 'public/signup.html', {'form': user_form})
