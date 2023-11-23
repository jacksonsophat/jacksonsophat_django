# Generated by Django 4.0.4 on 2023-11-09 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmazonPriceTracking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=750)),
                ('name', models.CharField(max_length=500)),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('expired_date', models.DateField()),
                ('contact_method', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=150)),
                ('phone', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
