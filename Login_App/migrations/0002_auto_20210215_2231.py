# Generated by Django 2.2.5 on 2021-02-15 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login_App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='full_name',
            new_name='fullname',
        ),
    ]
