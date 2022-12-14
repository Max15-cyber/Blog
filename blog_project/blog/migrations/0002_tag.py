# Generated by Django 4.1.3 on 2022-11-22 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50)),
                ('post_number', models.TextField(blank=True)),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
        ),
    ]
