# Generated by Django 4.1.4 on 2023-01-09 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0002_portfolio_blod_portfolio_medium_portfolio_regular_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='Blod',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='portfolio',
            old_name='Medium',
            new_name='fontname',
        ),
        migrations.RenameField(
            model_name='portfolio',
            old_name='Regular',
            new_name='textsize',
        ),
        migrations.RenameField(
            model_name='portfolio',
            old_name='SemiBold',
            new_name='totalpages',
        ),
    ]
