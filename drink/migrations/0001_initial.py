# Generated by Django 4.0.5 on 2022-06-03 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('description', models.TextField(max_length=256)),
            ],
            options={
                'db_table': 'my_category',
            },
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('nutrition', models.CharField(max_length=70)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drink.category')),
            ],
            options={
                'db_table': 'my_drink',
            },
        ),
    ]
