# Generated by Django 4.0.4 on 2022-05-10 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='thread',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='thread',
            name='first_person',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='second_person',
        ),
        migrations.DeleteModel(
            name='ChatMessage',
        ),
        migrations.DeleteModel(
            name='Thread',
        ),
    ]
