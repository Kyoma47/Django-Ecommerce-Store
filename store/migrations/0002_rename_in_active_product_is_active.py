# Generated by Django 5.1 on 2024-08-27 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='in_active',
            new_name='is_active',
        ),
    ]
