# Generated by Django 4.2.2 on 2023-06-22 21:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='client name')),
                ('comment', models.TextField(blank=True, max_length=500, null=True, verbose_name='comment about client')),
                ('email', models.EmailField(max_length=255, verbose_name='client mail')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=50, verbose_name='message theme')),
                ('body', models.TextField(max_length=500, verbose_name='message body')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='transmission name')),
                ('time', models.DateTimeField(default=datetime.datetime(2023, 1, 1, 0, 0), verbose_name='start time for sending')),
                ('frequency', models.CharField(choices=[('DAILY', 'Daily'), ('WEEKLY', 'Weekly'), ('MONTHLY', 'Monthly')])),
                ('status', models.CharField(choices=[('FINISHED', 'Finished'), ('CREATED', 'Created'), ('RUNNING', 'Running')], default='CREATED')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='transmission slug')),
                ('clients', models.ManyToManyField(to='mailing.clients')),
                ('message', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mailing.messages')),
            ],
            options={
                'verbose_name': 'Transmission',
                'verbose_name_plural': 'Transmission Templates',
            },
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(blank=True, default=None, null=True, verbose_name='last time for send')),
                ('status', models.CharField(choices=[('FINISHED', 'Finished'), ('CREATED', 'Created')], default='CREATED')),
                ('mail_answer', models.CharField(blank=True, default=None, null=True, verbose_name='answer from mailserver')),
                ('transmission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.transmission')),
            ],
            options={
                'verbose_name': 'Statistic',
                'verbose_name_plural': 'Statistics',
            },
        ),
    ]
