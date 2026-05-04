from django.db import models
from django.core.validators import RegexValidator

email_regex_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
    message='Enter a valid email address.'
)

name_validator = RegexValidator(
    regex=r'^[A-Za-z]+$',
    message='Only alphabetic characters are allowed.'
)

phone_validator = RegexValidator(
    regex=r'^[6-9]\d{9}$',
    message='Enter a valid 10-digit phone number starting with 6-9.'
)


class Member(models.Model):
  
  # firstname = models.CharField(max_length=255)
  # lastname = models.CharField(max_length=255)
  # # email = models.EmailField(null=False, unique=True)
  # email = models.EmailField(validators=[email_regex_validator], unique=True)  # optional: unique=True
  firstname = models.CharField(max_length=255, validators=[name_validator])
  lastname = models.CharField(max_length=255, validators=[name_validator])
  email = models.EmailField(validators=[email_regex_validator], unique=True)
  phone = models.CharField(max_length=10, unique=True, validators=[phone_validator])

  
  def __str__(self):
        return f"{self.firstname} {self.lastname} {self.email} {self.phone}"

# Create your models here.
