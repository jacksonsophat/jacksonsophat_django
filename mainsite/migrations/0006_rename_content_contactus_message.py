# Generated by Django 4.0.4 on 2023-11-23 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_contactus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='content',
            new_name='message',
        ),
    ]