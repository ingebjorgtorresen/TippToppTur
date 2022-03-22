from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brukere', '0008_merge_20220317_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turgåere',
            name='fødselsdato',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Fødselsdato'),
        ),
    ]
