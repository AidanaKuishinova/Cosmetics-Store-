# Generated by Django 4.0.2 on 2022-03-29 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=60, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField()),
                ('image', models.CharField(blank=True, max_length=100, null=True, verbose_name='Файл')),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('brand', models.CharField(blank=True, max_length=60, null=True)),
                ('country', models.CharField(blank=True, max_length=60, null=True)),
                ('ingredients', models.TextField(blank=True, null=True)),
                ('problems', models.TextField(blank=True, null=True)),
                ('type_of_skin', models.TextField(blank=True, null=True)),
                ('category', models.ManyToManyField(blank=True, null=True, to='main.Category')),
            ],
        ),
    ]
