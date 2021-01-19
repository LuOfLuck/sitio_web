# Generated by Django 2.2.3 on 2020-12-29 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.CharField(max_length=50)),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'comentario',
                'verbose_name_plural': 'comentarios',
            },
        ),
    ]