# Generated by Django 4.1.4 on 2023-01-05 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_team_detail_addtime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team_detail',
            old_name='addtime',
            new_name='add_time',
        ),
    ]
