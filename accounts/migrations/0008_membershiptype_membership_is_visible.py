# Generated by Django 4.0.4 on 2022-05-16 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_membershipbenefit_membership_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='membershiptype',
            name='membership_is_visible',
            field=models.BooleanField(default=True, verbose_name='Should we list this membership on the website?'),
        ),
    ]
