# Generated by Django 4.1.4 on 2023-01-05 18:43

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=100)),
                ('Aimage', models.ImageField(upload_to='author')),
                ('title', models.CharField(max_length=100)),
                ('content', froala_editor.fields.FroalaField(max_length=1000)),
                ('BTimage', models.ImageField(upload_to='blogthumb')),
                ('Bimage', models.ImageField(upload_to='blog')),
                ('url', models.CharField(max_length=100)),
            ],
        ),
    ]
