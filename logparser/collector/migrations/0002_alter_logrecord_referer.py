# Generated by Django 3.2 on 2021-04-20 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logrecord',
            name='referer',
            field=models.URLField(max_length=1000, null=True),
        ),
    ]