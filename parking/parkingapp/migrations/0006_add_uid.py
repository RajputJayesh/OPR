# Generated by Django 4.1.7 on 2023-04-11 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkingapp', '0005_alter_add_created_on_alter_add_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='add',
            name='uid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
