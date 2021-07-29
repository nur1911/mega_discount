# Generated by Django 3.2.5 on 2021-07-29 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=50, verbose_name='Адресс')),
                ('longitude', models.CharField(max_length=100, verbose_name='Долгота')),
                ('latitude', models.CharField(max_length=100, verbose_name='Широта')),
            ],
        ),
        migrations.CreateModel(
            name='Categori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название категории')),
                ('order_num', models.IntegerField(verbose_name='Очередность')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название города')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20, unique=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discount.city')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название компании')),
                ('photo', models.URLField()),
                ('description', models.TextField(verbose_name='Описание компании')),
                ('working_hours', models.CharField(max_length=20, verbose_name='Рабочие часы')),
                ('pin', models.CharField(max_length=4, verbose_name='Пин-код')),
                ('adress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discount.adress')),
                ('categori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discount.categori')),
            ],
        ),
        migrations.CreateModel(
            name='Discriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discriptions', models.TextField(verbose_name='Условия')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discount.company')),
            ],
        ),
        migrations.CreateModel(
            name='SocialNetworks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urls', models.URLField()),
                ('type', models.CharField(choices=[('INSTAGRAM', 'i'), ('VKONTAKTE', 'v'), ('FACEBOOK', 'f')], max_length=20)),
                ('logo', models.URLField()),
                ('active', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discount.company')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(verbose_name='Отзыв от клиента')),
                ('date_time', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discount.company')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discount.company')),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Дата начало')),
                ('end_date', models.DateField(verbose_name='Дата окончания')),
                ('percent', models.IntegerField(verbose_name='Процент скидки')),
                ('status', models.CharField(choices=[('ACTIVE', 'АКТИВНЫЙ'), ('CLOSED', 'НЕАКТИВНЫЙ')], max_length=10)),
                ('order_num', models.IntegerField()),
                ('discric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discount.discriptions')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='discount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discount.discount'),
        ),
        migrations.CreateModel(
            name='ClientDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateField()),
                ('status', models.CharField(choices=[('ACTIVE', 'АКТИВНЫЙ'), ('CLOSED', 'НЕАКТИВНЫЙ')], max_length=10, verbose_name='Статус')),
                ('edit_date', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discount.client')),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discount.discount')),
            ],
        ),
        migrations.AddField(
            model_name='adress',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discount.city'),
        ),
    ]
