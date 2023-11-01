# Generated by Django 4.2.7 on 2023-11-01 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgendaApp', '0003_agenda_estado_civil_alter_agenda_datanascimento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='estado',
            field=models.CharField(choices=[('SP', 'São Paulo'), ('MG', 'Minas Gerais'), ('RJ', 'Rio de Janeiro'), ('Es', 'Espírito Santo')], max_length=2),
        ),
    ]
