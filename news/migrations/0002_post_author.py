# Generated by Django 5.2.1 on 2025-05-10 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='author', max_length=150),
            preserve_default=False,
        ),
    ]
