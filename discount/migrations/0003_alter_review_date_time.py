# Generated by Django 3.2.5 on 2021-07-27 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0002_auto_20210727_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_time',
            field=models.DateField(auto_now=True),
        ),
    ]
