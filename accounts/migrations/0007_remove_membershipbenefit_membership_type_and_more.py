# Generated by Django 4.0.4 on 2022-05-16 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_membershipbenefit_benefit_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membershipbenefit',
            name='membership_type',
        ),
        migrations.AddField(
            model_name='membershipbenefit',
            name='membership_type',
            field=models.ManyToManyField(to='accounts.membershiptype'),
        ),
    ]
