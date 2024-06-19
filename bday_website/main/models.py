from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\d{9,15}$',
                message="Номер телефона должен содержать от 9 до 15 цифр."
            ),
        ]
    )
    message = models.TextField(blank=True, null=True)