# Generated by Django 4.2.16 on 2024-10-07 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('splash', '0002_remove_prospect_published_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prospect',
            name='subject',
        ),
    ]
