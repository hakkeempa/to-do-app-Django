# Generated by Django 4.0.2 on 2022-05-31 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='status',
            field=models.CharField(default='Incomplete', max_length=100),
        ),
    ]