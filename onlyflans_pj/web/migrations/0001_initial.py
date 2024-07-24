# Generated by Django 5.0.7 on 2024-07-17 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flan_uuid', models.UUIDField()),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(default='')),
                ('image_url', models.URLField(default='')),
                ('slug', models.SlugField(default='')),
                ('is_private', models.BooleanField(default=True)),
            ],
        ),
    ]
