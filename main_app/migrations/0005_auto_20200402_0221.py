# Generated by Django 3.0.4 on 2020-04-02 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20200402_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nest',
            name='broods',
            field=models.CharField(max_length=20, verbose_name='number of broods'),
        ),
        migrations.AlterField(
            model_name='nest',
            name='incubation',
            field=models.CharField(max_length=20, verbose_name='incubation period'),
        ),
    ]
