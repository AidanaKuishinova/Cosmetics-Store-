# Generated by Django 4.0.2 on 2022-03-29 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='url',
            field=models.CharField(default='none', max_length=60),
            preserve_default=False,
        ),
    ]
