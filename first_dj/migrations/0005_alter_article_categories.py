# Generated by Django 3.2 on 2022-12-23 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_dj', '0004_auto_20221223_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(related_name='articles', to='first_dj.Category'),
        ),
    ]