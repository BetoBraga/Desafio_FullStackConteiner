# Generated by Django 4.1.1 on 2022-10-01 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conteiner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cliente', models.CharField(max_length=100)),
                ('num_conteiner', models.CharField(max_length=12)),
                ('tipo_conteiner', models.IntegerField(max_length=41)),
                ('status_conteiner', models.CharField(max_length=6)),
                ('categoria_conteiner', models.CharField(max_length=11)),
            ],
        ),
    ]
