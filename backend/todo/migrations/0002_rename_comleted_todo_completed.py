# Generated by Django 4.0.3 on 2023-10-02 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='comleted',
            new_name='completed',
        ),
    ]
