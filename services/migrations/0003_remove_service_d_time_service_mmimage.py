# Generated by Django 4.1.4 on 2023-01-11 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_rename_portfolio_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='d_time',
        ),
        migrations.AddField(
            model_name='service',
            name='mmimage',
            field=models.ImageField(default=1, upload_to='portfoliothumb'),
            preserve_default=False,
        ),
    ]
