# Generated by Django 5.1 on 2024-11-17 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_commentmodel_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='full_name',
            field=models.CharField(max_length=100, verbose_name='full_name'),
        ),
    ]
