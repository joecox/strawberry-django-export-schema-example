from typing import Optional

import strawberry
from strawberry import auto

from ..books import models
from .series import Series
from .author import Author

@strawberry.django.type(models.Book)
class Book:
    title: auto
    author: Author
    series: Optional[Series]

@strawberry.type
class Query:
    books: list[Book] = strawberry.django.field()

schema = strawberry.Schema(
    query=Query
)