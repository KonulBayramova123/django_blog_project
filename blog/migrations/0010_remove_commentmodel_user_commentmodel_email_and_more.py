# Generated by Django 5.1 on 2024-11-17 14:29

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_merge_20241114_1733'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentmodel',
            name='user',
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='email'),
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='full_name',
            field=models.CharField(default='Anonymous user', max_length=100, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='categories',
            field=models.ManyToManyField(related_name='articles', to='blog.categorymodel', verbose_name='categories'),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, verbose_name='modified_at'),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='picture',
            field=models.ImageField(upload_to='article_images', verbose_name='picture'),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='published_at'),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='tags',
            field=models.ManyToManyField(related_name='articles', to='blog.tagmodel', verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.articlemodel', verbose_name='article'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='content',
            field=models.TextField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='contactusmodel',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned', to=settings.AUTH_USER_MODEL, verbose_name='assigned_to'),
        ),
        migrations.AlterField(
            model_name='contactusmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='contactusmodel',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='contactusmodel',
            name='message',
            field=models.TextField(verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='contactusmodel',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, verbose_name='modified_at'),
        ),
        migrations.AlterField(
            model_name='contactusmodel',
            name='resolved_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='resolved_at'),
        ),
        migrations.AlterField(
            model_name='contactusmodel',
            name='stage',
            field=models.CharField(choices=[('new', 'New'), ('in_review', 'In Review'), ('in_progress', 'In Progress'), ('resolved', 'Resolved'), ('closed', 'Closed')], default='new', max_length=20, verbose_name='stage'),
        ),
        migrations.AlterField(
            model_name='contactusmodel',
            name='subject',
            field=models.CharField(max_length=200, verbose_name='subject'),
        ),
        migrations.AlterField(
            model_name='tagmodel',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='tagmodel',
            name='name',
            field=models.CharField(max_length=150, verbose_name='name'),
        ),
    ]
