# Generated by Django 4.1 on 2022-08-19 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_alter_scopes_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scopes',
            old_name='main',
            new_name='is_main',
        ),
    ]
