# Generated by Django 2.2.5 on 2019-09-14 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20190914_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admitcard',
            name='link',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='admitcard',
            name='title',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='answerkey',
            name='link',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='answerkey',
            name='title',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='eligibility',
            name='criteria',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='eligibility',
            name='title',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='event',
            name='min_education_qualification',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='description',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='name',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_title',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_title',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='fee',
            name='title',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='howto',
            name='title',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='importantdate',
            name='title',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='importantlink',
            name='link',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='importantlink',
            name='title',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='importantupdate',
            name='title',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='result',
            name='link',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='title',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='link',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='title',
            field=models.CharField(max_length=5000),
        ),
    ]
