# Generated by Django 3.2.20 on 2024-03-03 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DeliveryApp', '0007_delivery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_type', models.CharField(max_length=50)),
                ('image_file', models.CharField(max_length=300)),
                ('delivery', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='DeliveryApp.delivery')),
            ],
        ),
    ]
