# Generated by Django 3.1.1 on 2020-09-08 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_pub',
            new_name='pub_date',
        ),
    ]
