# Generated by Django 3.2.20 on 2024-03-03 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DeliveryApp', '0003_deliveryperson_profile_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliveryperson_profile',
            old_name='Name',
            new_name='Username',
        ),
        migrations.RemoveField(
            model_name='deliveryperson_profile',
            name='Gender',
        ),
        migrations.RemoveField(
            model_name='deliveryperson_profile',
            name='PhoneNo',
        ),
    ]