# Generated by Django 3.2.7 on 2021-09-14 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0010_alter_journalresource_contactnames'),
    ]

    operations = [
        migrations.AddField(
            model_name='journalresource',
            name='studied',
            field=models.BooleanField(default=False),
        ),
    ]
