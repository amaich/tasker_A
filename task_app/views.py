from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.base import ContextMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import *

from .forms import *


def start_page(request):
    return render(request, 'task_app/index.html', {})


class TaskListView(ListView):
    model = TaskModel
    template_name = 'task_app/task_list.html'
    context_object_name = 'tasks'
    queryset = TaskModel.objects.all()[:10]


class TaskDetailView(DetailView):
    model = TaskModel
    template_name = 'task_app/task_detail.html'
    context_object_name = 'task'


class TaskCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'task_app/task_create.html', {'form': form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = TaskModel(summary=form.cleaned_data['summary'],
                                 description=form.cleaned_data['description'],
                                 slug=form.cleaned_data['slug'],)
            new_task.save()
            return HttpResponseRedirect(reverse('task_app:task_detail', kwargs={'slug': request.POST.get('slug')}))


class TaskUpdateView(View):
    extra_context = {'username': 'SOSO_BITCH'}
    context = {}

    def get(self, request, slug):
        update_task = get_object_or_404(TaskModel, slug=slug)
        form = TaskForm(instance=update_task)
        self.context['form'] = form
        self.context['task'] = update_task
        self.context = super().add_extra_context()
        return render(request, 'task_app/task_update.html', self.context)

    def post(self, request, slug):
        update_task = get_object_or_404(TaskModel, slug=slug)
        form = TaskForm(request.POST, instance=update_task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task_app:task_detail', kwargs={'slug': request.POST.get('slug')}))


class TaskDeleteView(View):
    def get(self, request, slug):
        delete_task = get_object_or_404(TaskModel, slug=slug)
        delete_task.delete()
        return HttpResponseRedirect(reverse('task_app:task_list'))

