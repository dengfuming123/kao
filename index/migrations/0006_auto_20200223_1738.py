# Generated by Django 2.1.15 on 2020-02-23 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_remove_post_comment_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
