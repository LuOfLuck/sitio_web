# Generated by Django 2.2.3 on 2021-01-05 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('informacion', '0012_auto_20210103_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='persona',
        ),
    ]
