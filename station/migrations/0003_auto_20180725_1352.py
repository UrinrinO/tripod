# Generated by Django 2.0.7 on 2018-07-25 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0002_auto_20180724_1859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='surname',
            new_name='last_name',
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(blank=True, max_length=14),
        ),
    ]
