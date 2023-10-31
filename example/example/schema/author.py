import strawberry
from strawberry import auto

from ..books import models


@strawberry.django.type(models.Author)
class Author:
    name: auto