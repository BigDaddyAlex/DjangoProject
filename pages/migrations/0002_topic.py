# Generated by Django 3.0.7 on 2020-06-19 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=30)),
                ('topic_TLDR', models.CharField(max_length=30)),
                ('topic_body', models.CharField(max_length=1000)),
                ('topic_last_modified', models.DateTimeField()),
            ],
        ),
    ]
