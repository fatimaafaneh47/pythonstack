# Generated by Django 2.2.4 on 2022-09-28 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semiapp', '0002_auto_20220928_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]
