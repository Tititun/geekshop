# Generated by Django 3.2.9 on 2021-12-23 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='create',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='update',
            new_name='updated',
        ),
    ]
