# Generated by Django 3.2.3 on 2023-12-27 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_rename_contnet_post_contet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='contet',
            new_name='content',
        ),
    ]
