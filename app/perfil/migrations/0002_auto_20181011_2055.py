# Generated by Django 2.1.2 on 2018-10-11 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='endereco',
            field=models.CharField(blank=True, default='RUA 1', max_length=255),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='idade',
            field=models.IntegerField(default=2),
        ),
    ]