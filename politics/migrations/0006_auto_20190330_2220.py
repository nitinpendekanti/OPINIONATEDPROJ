# Generated by Django 2.1.2 on 2019-03-30 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('politics', '0005_debate_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='debate',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='voting',
            name='debate2',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.DeleteModel(
            name='likes',
        ),
        migrations.DeleteModel(
            name='Voting',
        ),
    ]