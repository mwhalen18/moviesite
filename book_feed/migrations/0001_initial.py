# Generated by Django 4.2.3 on 2023-08-03 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1000)),
                ('authors', models.TextField(default='')),
                ('pub_date', models.CharField(max_length=10)),
                ('description', models.TextField(default='')),
                ('cover_path', models.URLField(default='')),
            ],
        ),
    ]
