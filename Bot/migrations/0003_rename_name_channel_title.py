# Generated by Django 4.2 on 2023-05-04 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bot', '0002_rename_channels_channel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channel',
            old_name='name',
            new_name='title',
        ),
    ]
