# Generated by Django 5.1 on 2024-11-06 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_contactusmodel_resolved_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='categories',
            field=models.ManyToManyField(related_name='articles', to='blog.categorymodel'),
        ),
    ]
