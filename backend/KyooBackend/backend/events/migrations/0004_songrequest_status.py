# Generated by Django 4.2.6 on 2023-10-28 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_remove_event_qr_code_songrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='songrequest',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10),
        ),
    ]
