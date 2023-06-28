# Generated by Django 4.2.2 on 2023-06-28 23:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transmission',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='transmission',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='start time for sending'),
        ),
    ]
