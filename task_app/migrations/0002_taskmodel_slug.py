# Generated by Django 4.2 on 2023-04-25 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='slug',
            field=models.SlugField(default='test1'),
            preserve_default=False,
        ),
    ]
