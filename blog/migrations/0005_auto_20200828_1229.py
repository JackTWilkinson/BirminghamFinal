# Generated by Django 2.2.15 on 2020-08-28 17:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200826_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2020, 8, 28, 17, 29, 24, 571256, tzinfo=utc)),
        ),
    ]