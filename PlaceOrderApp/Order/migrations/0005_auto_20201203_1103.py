# Generated by Django 3.1.3 on 2020-12-03 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0004_auto_20201202_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdata',
            name='delete_date',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='formdata',
            name='edit_date',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='formdata',
            name='update_date',
            field=models.CharField(default='', max_length=500, null=True),
        ),
    ]
