# Generated by Django 5.0.4 on 2024-05-09 12:58

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('city', models.CharField(blank=True, max_length=56, null=True)),
                ('salary', models.CharField(blank=True, max_length=40, null=True)),
                ('schedule', models.CharField(blank=True, max_length=100, null=True)),
                ('details', models.JSONField(blank=True, default=list, null=True)),
                ('skills', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Job Listing',
                'verbose_name_plural': 'Job Listings',
            },
        ),
    ]