# Generated by Django 4.0.1 on 2022-02-28 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0003_alter_payment_crno'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=1000)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Order',
            },
        ),
    ]
