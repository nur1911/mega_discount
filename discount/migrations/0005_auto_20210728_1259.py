# Generated by Django 3.2.5 on 2021-07-28 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0004_auto_20210728_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='order_num',
        ),
        migrations.RemoveField(
            model_name='company',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='company',
            name='reviews',
        ),
        migrations.RemoveField(
            model_name='company',
            name='views',
        ),
        migrations.AddField(
            model_name='categori',
            name='order_num',
            field=models.IntegerField(default=1, verbose_name='Очередность'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='discount.company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='discount.company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='view',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='discount.company'),
            preserve_default=False,
        ),
    ]
