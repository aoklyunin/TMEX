# -*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse, HttpResponseBadRequest, Http404, \
    HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.template import RequestContext


def permissionDenied(request):
    return render(request, 'permissionDenied.html', {})


def frontPage(request):
    return render(request, 'public/front_page.html', {'flgMainPage': True})


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


def is_moderator(user):
    return user.groups.filter(name='moderators').exists()

