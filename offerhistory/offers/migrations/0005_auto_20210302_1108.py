# Generated by Django 3.1.7 on 2021-03-02 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0004_auto_20210302_1032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='carnake',
            new_name='carmake',
        ),
    ]
