# Generated by Django 4.0.4 on 2022-05-16 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_usermembership_discretionary_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membershipbenefit',
            name='benefit_details',
            field=models.TextField(blank=True, null=True),
        ),
    ]
