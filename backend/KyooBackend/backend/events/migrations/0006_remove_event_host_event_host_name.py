# Generated by Django 4.2.6 on 2023-10-29 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_remove_songrequest_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='host',
        ),
        migrations.AddField(
            model_name='event',
            name='host_name',
            field=models.CharField(default='The Host', max_length=255),
        ),
    ]
