# Generated by Django 3.0.4 on 2020-04-06 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_finch_similar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finch',
            name='conservation',
            field=models.CharField(max_length=100, verbose_name='conservation concern'),
        ),
    ]
