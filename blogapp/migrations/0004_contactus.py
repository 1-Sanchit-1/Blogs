# Generated by Django 3.2.3 on 2024-01-12 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_rename_contet_post_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=1000)),
                ('Message', models.CharField(max_length=5000)),
            ],
            options={
                'verbose_name': 'Contact-form',
                'verbose_name_plural': 's',
            },
        ),
    ]
