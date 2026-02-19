from django.core.validators import RegexValidator
from django.db import models
from rest_framework.fields import JSONField

from protocol_api.study import Study


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
    study_definition = models.JSONField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._study = None

    @property
    def study(self) -> Study:
        if self._study is None:
            self._study = Study(self.study_definition)
        return self._study

