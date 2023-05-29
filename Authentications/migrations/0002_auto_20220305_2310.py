# Generated by Django 2.2.26 on 2022-03-05 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('acountNo', models.CharField(default=None, max_length=256)),
                ('first_name', models.CharField(default=None, max_length=100)),
                ('last_name', models.CharField(default=None, max_length=100)),
                ('email', models.CharField(default=None, max_length=100)),
                ('tariff', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]