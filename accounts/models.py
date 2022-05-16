# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    first_visit = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


    def __str__(self):
        return self.username

class MembershipType(models.Model):
    membership_title = models.CharField(max_length=100)
    membership_description = models.CharField(max_length=100)
    membership_monthly_cost = models.FloatField()
    membership_annual_discount_percentage = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.membership_title

class MembershipBenefit(models.Model):
    benefit_title = models.CharField(max_length=100)
    benefit_details = models.TextField(null=True, blank=True)
    membership_type = models.ManyToManyField(MembershipType)

    def __str__(self):
        return self.benefit_title

class UserMembership(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    membershiptype = models.ForeignKey(MembershipType, on_delete=models.CASCADE)
    signed_up_date = models.DateField()
    cancelled_date = models.DateField(null=True, blank=True)
    discretionary_discount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.membershiptype.membership_title}"
