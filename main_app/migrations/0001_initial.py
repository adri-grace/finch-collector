# Generated by Django 3.0.4 on 2020-03-26 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variety', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('habitat', models.CharField(max_length=100)),
                ('food', models.CharField(max_length=100)),
                ('nesting', models.CharField(max_length=100)),
                ('behavior', models.CharField(max_length=100)),
                ('conservation', models.CharField(max_length=100)),
            ],
        ),
    ]
