# Generated by Django 4.0.2 on 2022-03-15 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brukere', '0006_turgåere_fødselsdato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turgåere',
            name='fødselsdato',
            field=models.DateField(verbose_name='Fødselsdato'),
        ),
    ]
