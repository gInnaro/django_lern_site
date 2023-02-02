# Generated by Django 4.1.5 on 2023-01-30 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_alter_todolist_created_alter_todolist_due_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категории', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='todolist',
            options={'ordering': ['-created'], 'verbose_name': 'Список дел', 'verbose_name_plural': 'Список дел'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='content',
            field=models.TextField(blank=True, verbose_name='Содержимое'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default='2023-01-30', verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(default='2023-01-30', verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Название'),
        ),
    ]