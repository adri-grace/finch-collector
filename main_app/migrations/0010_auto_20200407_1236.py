# Generated by Django 3.0.4 on 2020-04-07 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='cat',
            new_name='finch',
        ),
    ]