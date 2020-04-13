from django.db import models

# Create your models here.
""" model for a user"""


class Account(models.Model):
    first_name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)
    emailid = models.EmailField(blank=False, null=False, unique=True)
    password = models.CharField(max_length=255, blank=False, null=False)
    number = models.CharField(max_length=13, blank=False, null=False, unique=True)
    birth_date = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.emailid


""" model for a user's address"""


class Address(models.Model):
    title = models.CharField(max_length=20, blank=False, null=False)
    user = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="user_address"
    )
    address = models.CharField(max_length=250, blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)
    state = models.CharField(max_length=50, blank=False, null=False)
    pin_code = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.title
