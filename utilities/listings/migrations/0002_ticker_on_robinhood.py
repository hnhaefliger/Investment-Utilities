# Generated by Django 3.2.7 on 2021-09-27 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='on_robinhood',
            field=models.BooleanField(default=False),
        ),
    ]
