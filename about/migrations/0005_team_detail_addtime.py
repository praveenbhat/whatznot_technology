# Generated by Django 4.1.4 on 2023-01-05 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_alter_team_detail_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='team_detail',
            name='addtime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
