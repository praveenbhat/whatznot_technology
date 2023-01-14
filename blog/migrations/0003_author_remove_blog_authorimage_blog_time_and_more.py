# Generated by Django 4.1.4 on 2023-01-05 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_aimage_blog_authorimage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=100)),
                ('authorimage', models.ImageField(upload_to='author')),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='authorimage',
        ),
        migrations.AddField(
            model_name='blog',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.author'),
        ),
    ]
