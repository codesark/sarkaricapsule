# Generated by Django 2.2.5 on 2019-11-17 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_event_create_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='create_news',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Create News??'),
        ),
    ]
