# Generated by Django 2.2.3 on 2021-01-05 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promociones', '0007_estudiante_mensaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='mensaje',
            field=models.CharField(default='era una persona de pocas palabras, le deseamos lo mejor', max_length=250),
        ),
    ]
