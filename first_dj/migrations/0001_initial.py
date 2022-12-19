# Generated by Django 3.2.16 on 2022-12-15 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=128, verbose_name='Titel')),
                ('is_published', models.BooleanField(default=True, verbose_name='Is Published')),
                ('content', models.TextField(verbose_name='Content')),
            ],
        ),
    ]