# Generated by Django 4.1.1 on 2022-10-01 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_conteiner_tipo_conteiner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conteiner',
            name='categoria_conteiner',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='conteiner',
            name='num_conteiner',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='conteiner',
            name='status_conteiner',
            field=models.CharField(max_length=5),
        ),
    ]
