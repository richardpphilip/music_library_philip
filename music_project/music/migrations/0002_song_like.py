# Generated by Django 3.1.7 on 2021-04-16 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='like',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
