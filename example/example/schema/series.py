import strawberry
from strawberry import auto

from ..books import models
from .author import Author


@strawberry.django.type(models.Series)
class Series:
    name: auto
    author: Author