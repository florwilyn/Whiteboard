# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-20 02:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owns', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='whiteboard.Group')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_a_member_of', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='whiteboard.Group')),
            ],
        ),
        migrations.AddField(
            model_name='chat',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='whiteboard.Group'),
        ),
        migrations.AddField(
            model_name='chat',
            name='sender',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
