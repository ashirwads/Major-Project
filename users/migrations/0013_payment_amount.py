# Generated by Django 3.0.5 on 2020-04-26 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200426_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.CharField(default=0, max_length=20),
        ),
    ]