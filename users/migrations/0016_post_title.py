# Generated by Django 3.0.5 on 2020-06-09 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Add your title', max_length=100),
        ),
    ]