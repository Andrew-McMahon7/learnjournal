# Generated by Django 3.2.7 on 2021-09-13 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0009_alter_journalresource_contactnames'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalresource',
            name='contactNames',
            field=models.ManyToManyField(blank=True, to='journal.ContactsResource'),
        ),
    ]
