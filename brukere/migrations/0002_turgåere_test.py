# Generated by Django 4.0.2 on 2022-02-10 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brukere', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turgåere',
            name='test',
            field=models.TextField(blank=True),
        ),
    ]
