# Generated by Django 2.2.26 on 2022-03-05 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authentications', '0003_auto_20220305_2323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newuser',
            old_name='username',
            new_name='mobileNo',
        ),
    ]