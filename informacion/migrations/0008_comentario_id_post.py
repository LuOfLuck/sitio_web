# Generated by Django 2.2.3 on 2021-01-03 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informacion', '0007_comentario_persona'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='id_post',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
