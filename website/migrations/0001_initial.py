# Generated by Django 4.2.1 on 2023-06-05 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=225)),
                ('number_of_trainings', models.IntegerField()),
                ('cost', models.IntegerField()),
            ],
            options={
                'verbose_name': 'price',
                'verbose_name_plural': 'prices',
                'ordering': ('number_of_trainings', 'cost'),
            },
        ),
    ]
