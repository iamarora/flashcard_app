from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel


class BaseModel(TimeStampedModel, SoftDeletableModel):

    all_objects = models.Manager()

    class Meta:
        abstract = True
