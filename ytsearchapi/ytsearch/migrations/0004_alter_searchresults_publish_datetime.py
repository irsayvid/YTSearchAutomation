# Generated by Django 4.0 on 2021-12-22 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ytsearch', '0003_remove_searchresults_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchresults',
            name='publish_datetime',
            field=models.DateTimeField(null=True),
        ),
    ]
