# Generated by Django 2.2.17 on 2020-11-20 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_list', '0007_auto_20201120_1731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor_list',
            old_name='estoque',
            new_name='stock',
        ),
    ]
