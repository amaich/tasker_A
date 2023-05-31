from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


class UserLogin(View):
    def get(self, request):
        return render(request, 'task_auth/login.html', {})

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('task_app:task_list', kwargs={}))
        else:
            return HttpResponse('nea')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('task_auth:auth_check', kwargs={}))


def is_auth_check(request):
    return HttpResponse('You are logged in: ' + str(request.user.is_authenticated))
