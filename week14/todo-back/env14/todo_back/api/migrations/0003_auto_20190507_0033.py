# Generated by Django 2.2.1 on 2019-05-06 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190506_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='api.TaskList'),
        ),
    ]
