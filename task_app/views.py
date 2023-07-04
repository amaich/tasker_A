from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import TaskModel

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


class TaskCreateView(CreateView):
    model = TaskModel
    template_name = 'task_app/task_create.html'
    fields = ['summary', 'description', 'assignee']
    success_url = reverse_lazy('task_app:task_list')


class TaskUpdateView(UpdateView):
    model = TaskModel
    template_name = 'task_app/task_update.html'
    fields = ['summary', 'description', 'assignee']
    success_url = reverse_lazy('task_app:task_list')
    context_object_name = 'task'


class TaskDeleteView(DeleteView):
    model = TaskModel
    success_url = reverse_lazy('task_app:task_list')


# class TaskCreateView(LoginRequiredMixin, View):
#     def get(self, request):
#         form = TaskForm()
#         return render(request, 'task_app/task_create.html', {'form': form})
#
#     def post(self, request):
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             new_task = TaskModel(summary=form.cleaned_data['summary'],
#                                  description=form.cleaned_data['description'],
#                                  slug=form.cleaned_data['slug'],)
#             new_task.save()
#             return HttpResponseRedirect(reverse('task_app:task_detail', kwargs={'slug': request.POST.get('slug')}))
# class TaskUpdateView(View):
#     def get(self, request, pk):
#         update_task = get_object_or_404(TaskModel, pk=pk)
#         form = TaskForm(instance=update_task)
#         return render(request, 'task_app/task_update.html', {'form': form, 'task': update_task})
#
#     def post(self, request, pk):
#         update_task = get_object_or_404(TaskModel, pk=pk)
#         form = TaskForm(request.POST, instance=update_task)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('task_app:task_detail', kwargs={'pk': pk}))

# class TaskDeleteView(View):
#     def get(self, request, pk):
#         delete_task = get_object_or_404(TaskModel, pk=pk)
#         delete_task.delete()
#         return HttpResponseRedirect(reverse('task_app:task_list'))
