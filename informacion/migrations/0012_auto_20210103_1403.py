# Generated by Django 2.2.3 on 2021-01-03 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informacion', '0011_auto_20210102_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=models.TextField(),
        ),
    ]
