# Generated by Django 3.2.20 on 2024-03-02 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DeliveryApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='Password',
            field=models.CharField(max_length=130),
        ),
        migrations.AlterField(
            model_name='login',
            name='UserType',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='login',
            name='Username',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.CreateModel(
            name='DeliveryPerson_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Gender', models.CharField(max_length=150)),
                ('Email', models.CharField(max_length=250)),
                ('PhoneNo', models.BigIntegerField()),
                ('LOGIN', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='DeliveryApp.login')),
            ],
        ),
    ]
