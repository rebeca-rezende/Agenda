# Generated by Django 4.2.6 on 2023-11-02 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AgendaApp', '0006_alter_agenda_cidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ddd', models.IntegerField(max_length=2)),
                ('numero', models.CharField(max_length=10)),
                ('tipo', models.CharField(choices=[('RES', 'Residencial'), ('COM', 'Comercial'), ('REC', 'Recado')], max_length=3)),
                ('IsWhatsapp', models.BooleanField(verbose_name='Tem Whatsapp? ')),
                ('contato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AgendaApp.agenda')),
            ],
        ),
    ]
