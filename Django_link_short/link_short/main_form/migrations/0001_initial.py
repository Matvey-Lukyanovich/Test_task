# Generated by Django 4.0.6 on 2022-07-27 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shortcut_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_info', models.CharField(max_length=50, verbose_name='Пользователь')),
                ('link_info', models.CharField(max_length=50, verbose_name='Начальная ссылка')),
                ('link_short', models.CharField(max_length=50, verbose_name='Конечная ссылка')),
            ],
        ),
    ]
