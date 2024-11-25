# Generated by Django 5.0.4 on 2024-05-19 06:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insurance', '0006_alter_ajents_end_time_alter_ajents_start_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ajents',
            name='Phone',
        ),
        migrations.RemoveField(
            model_name='ajents',
            name='age',
        ),
        migrations.RemoveField(
            model_name='ajents',
            name='date',
        ),
        migrations.RemoveField(
            model_name='ajents',
            name='end_Time',
        ),
        migrations.RemoveField(
            model_name='ajents',
            name='start_Time',
        ),
        migrations.AddField(
            model_name='ajents',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='ajents',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='ajents',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.CreateModel(
            name='AgentAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Insurance.ajents')),
            ],
            options={
                'unique_together': {('agent', 'date', 'start_time', 'end_time')},
            },
        ),
    ]
