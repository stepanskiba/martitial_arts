# Generated by Django 4.1.7 on 2023-06-04 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('algo_task', '0013_alter_abc_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='abc',
            options={'ordering': ('-id', '-M'), 'verbose_name': 'A_H_R_M', 'verbose_name_plural': 'A_H_R_M_S'},
        ),
    ]
