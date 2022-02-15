# Generated by Django 4.0.2 on 2022-02-15 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('space_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('space_description', models.CharField(max_length=1000)),
                ('space_image', models.ImageField(blank=True, upload_to='photos/spaces')),
                ('space_location', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
    ]