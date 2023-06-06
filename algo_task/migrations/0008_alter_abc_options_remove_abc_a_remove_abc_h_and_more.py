# Generated by Django 4.1.7 on 2023-06-04 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algo_task', '0007_alter_abc_options_alter_abc_a'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='abc',
            options={'ordering': ('id', '-a'), 'verbose_name': 'A_B_C', 'verbose_name_plural': 'A_B_C_S'},
        ),
        migrations.RemoveField(
            model_name='abc',
            name='A',
        ),
        migrations.RemoveField(
            model_name='abc',
            name='H',
        ),
        migrations.RemoveField(
            model_name='abc',
            name='M',
        ),
        migrations.RemoveField(
            model_name='abc',
            name='R',
        ),
        migrations.AddField(
            model_name='abc',
            name='b',
            field=models.IntegerField(default=0, help_text='Подсказка для поля B', verbose_name='Значение B'),
        ),
        migrations.AddField(
            model_name='abc',
            name='c',
            field=models.IntegerField(default=0, verbose_name='Значение С'),
        ),
        migrations.AlterField(
            model_name='abc',
            name='task',
            field=models.CharField(default='Равна ли С сумме A и B ?', max_length=255, verbose_name='Формулировка задачи'),
        ),
        migrations.AddField(
            model_name='abc',
            name='a',
            field=models.IntegerField(default=0, verbose_name='Значение А'),
        ),
    ]