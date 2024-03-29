# Generated by Django 3.2.20 on 2024-03-03 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DeliveryApp', '0006_alter_login_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_name', models.CharField(max_length=120)),
                ('delivery_date', models.DateTimeField(auto_now_add=True)),
                ('user_profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='DeliveryApp.deliveryperson_profile')),
            ],
        ),
    ]
