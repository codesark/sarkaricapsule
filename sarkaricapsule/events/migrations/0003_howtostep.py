# Generated by Django 2.2.5 on 2019-09-11 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_faq_howto'),
    ]

    operations = [
        migrations.CreateModel(
            name='HowToStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('howto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='events.HowTo')),
            ],
        ),
    ]
