from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class Protocol(models.Model):
    name = models.CharField(
        max_length=40,
        unique=True,  # Enforces uniqueness at DB level
        validators=[
            RegexValidator(
                regex=r'^[a-z0-9_]+$',
                message='Name must contain only lower case alphanumeric characters, and underscores',
                code='invalid_name'
            )
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
