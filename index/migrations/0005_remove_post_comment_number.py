# Generated by Django 2.1.15 on 2020-02-23 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_remove_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment_number',
        ),
    ]
