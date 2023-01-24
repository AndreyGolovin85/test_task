# Generated by Django 4.1.2 on 2023-01-24 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='Электронная почта')),
                ('country', models.CharField(max_length=60, verbose_name='Страна')),
                ('city', models.CharField(max_length=60, verbose_name='Город')),
                ('street', models.CharField(max_length=60, verbose_name='Улица')),
                ('number_home', models.CharField(max_length=10, verbose_name='Дом')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Название')),
                ('model', models.CharField(max_length=60, verbose_name='Модель')),
                ('data', models.DateField(max_length=10, verbose_name='Дата поступления в продажу')),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('arrears', models.FloatField(null=True, verbose_name='Задолженность')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('contacts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network.contacts', verbose_name='Контакты')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network.products', verbose_name='Продукция')),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='network.network', verbose_name='Задолженность')),
            ],
        ),
    ]