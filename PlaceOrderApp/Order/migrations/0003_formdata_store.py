# Generated by Django 3.1.3 on 2020-12-01 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_formdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdata',
            name='store',
            field=models.CharField(default='', editable=False, max_length=500),
        ),
    ]