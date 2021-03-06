# Generated by Django 3.1.3 on 2020-12-16 13:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.BinaryField(max_length=100)),
                ('price', models.IntegerField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('seller', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='seller.sell')),
            ],
        ),
    ]
