# Generated by Django 4.0.4 on 2022-05-18 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockkeeper', '0014_alter_component_sku'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='sku',
        ),
    ]
