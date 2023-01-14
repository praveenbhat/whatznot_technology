# Generated by Django 4.1.4 on 2023-01-09 19:35

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='portfolio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('d_time', models.DateTimeField()),
                ('type', models.CharField(max_length=1000)),
                ('client', models.CharField(max_length=1000)),
                ('himage', models.ImageField(upload_to='portfoliothumb')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=1000)),
                ('fdes', froala_editor.fields.FroalaField(max_length=1000)),
                ('vtitle', models.CharField(max_length=1000)),
                ('vdes', froala_editor.fields.FroalaField(max_length=1000)),
                ('bimage', models.ImageField(upload_to='bimage')),
                ('simage', models.ImageField(upload_to='simage')),
                ('ssimage', models.ImageField(upload_to='simage')),
                ('mimage', models.ImageField(upload_to='simage')),
                ('sssimage', models.ImageField(upload_to='simage')),
                ('ssssimage', models.ImageField(upload_to='simage')),
                ('lastcontent', froala_editor.fields.FroalaField(max_length=1000)),
                ('url', models.SlugField(max_length=100)),
            ],
        ),
    ]
