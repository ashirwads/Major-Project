# Generated by Django 3.0.5 on 2020-04-25 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200424_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='board',
            field=models.CharField(choices=[('CBSE', 'CBSE'), ('ICSE', 'ICSE'), ('STATE BOARD', 'STATE BOARD')], default='CBSE', max_length=20),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='course',
            field=models.CharField(choices=[('BTech', 'B.Tech'), ('MBA', 'MBA'), ('BPharma', 'B.Pharma'), ('DPharma', 'D.Pharma'), ('BBA', 'BBA'), ('Bcom', 'B.com')], default='BTech', max_length=20),
        ),
    ]