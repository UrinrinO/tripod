# Generated by Django 2.0.7 on 2018-07-24 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=255)),
                ('surname', models.CharField(blank=True, default='', max_length=255)),
                ('phone', models.TextField(blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]