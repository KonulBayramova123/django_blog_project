# Generated by Django 5.1 on 2024-10-29 16:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_commentmodel'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('stage', models.CharField(choices=[('new', 'New'), ('in_review', 'In Review'), ('in_progress', 'In Progress'), ('resolved', 'Resolved'), ('closed', 'Closed')], default='new', max_length=20)),
                ('resolved_at', models.DateTimeField(null=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ContactUs',
                'verbose_name_plural': 'ContactUs',
                'db_table': 'user_messages',
            },
        ),
    ]
