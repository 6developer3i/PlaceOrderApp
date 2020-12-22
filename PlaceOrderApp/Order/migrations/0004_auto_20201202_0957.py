# Generated by Django 3.1.3 on 2020-12-02 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0003_formdata_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopify',
            name='access_token',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='shopify',
            name='code',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='shopify',
            name='hmac',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='shopify',
            name='shop',
            field=models.CharField(max_length=2000),
        ),
    ]
