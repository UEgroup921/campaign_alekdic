# Generated by Django 3.1.1 on 2020-11-08 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0010_auto_20201107_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='roles',
            name='login_value',
            field=models.IntegerField(default=1, verbose_name='login_value'),
        ),
    ]