# Generated by Django 2.0.7 on 2018-07-25 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': [['can_view_goldpage', 'Can view goldpage']]},
        ),
    ]
