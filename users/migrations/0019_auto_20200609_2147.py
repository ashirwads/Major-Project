# Generated by Django 2.2.2 on 2020-06-09 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20200609_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(upload_to='media/'),
        ),
    ]