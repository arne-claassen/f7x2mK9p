from django.core.validators import RegexValidator
from django.db import models
from django.utils.functional import classproperty

from protocol_api.cache import ModelCache
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
    description = models.TextField(default="")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._study = None

    @property
    def study(self) -> Study:
        if self._study is None:
            self._study = Study(self.study_definition)
        return self._study


    @classproperty
    def instances(cls) -> ModelCache:
        # NOTE: This code HAS to use *attr because @classproperty does some magic that means that
        # setting and getting by dot notation actually does not happen on the class but is only a
        # local variable
        if not hasattr(cls, "__instances"):
            setattr(cls, '__instances', ModelCache(cls, 'name'))
        return getattr(cls, '__instances')
