# Generated by Django 3.1.3 on 2020-12-03 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0005_auto_20201203_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdata',
            name='build_date',
            field=models.CharField(default='', max_length=500),
        ),
    ]