# Generated by Django 3.2.20 on 2024-03-02 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=200)),
                ('Password', models.CharField(max_length=200)),
                ('UserType', models.CharField(max_length=200)),
            ],
        ),
    ]
