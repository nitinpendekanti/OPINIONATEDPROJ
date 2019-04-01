# Generated by Django 2.1.2 on 2019-02-01 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('politics', '0002_auto_20190116_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='comments',
            name='username',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='debate',
            name='date',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='debate',
            name='genre',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='debate',
            name='pfp',
            field=models.CharField(blank=True, default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='debate',
            name='picture',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='debate',
            name='title',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='debate',
            name='username',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
