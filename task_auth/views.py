from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
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
    return HttpResponseRedirect(reverse('task_app:task_list', kwargs={}))


class UserRegistration(View):
    def get(self, request):
        return render(request, 'task_auth/user_registration.html', {})

    def post(self, request):
        user = User.objects.create_user(username = request.POST["username"],
                                        password = request.POST["password"])
        user.save()
        if user is not None:
            return HttpResponseRedirect(reverse('task_auth:login'), kwargs={})
        else:
            return HttpResponse('nea')


def is_auth_check(request):
    return HttpResponse('You are logged in: ' + str(request.user.is_authenticated))
