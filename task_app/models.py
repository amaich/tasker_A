from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


class TaskModel(models.Model):
    summary = models.CharField(max_length=100, verbose_name='Summary')
    description = models.TextField(verbose_name='Description')
    assignee = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    slug = models.SlugField(null=False)

    def __str__(self):
        return self.summary

    def get_absolute_url(self):
        return reverse('task_app:task_detail', kwargs={'slug': self.slug})

