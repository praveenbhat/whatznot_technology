# Generated by Django 4.1.4 on 2023-01-13 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_rename_stags_service_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='ffimage',
            field=models.ImageField(default=1, upload_to='portfoliothumb'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='fimage',
            field=models.ImageField(default=1, upload_to='portfoliothumb'),
            preserve_default=False,
        ),
    ]
