from typing import Optional

import strawberry
import strawberry_django
from strawberry import auto

from .books import models


@strawberry_django.type(models.Author)
class Author:
    name: auto

@strawberry_django.type(models.Series)
class Series:
    name: auto
    author: Author

@strawberry_django.type(models.Book)
class Book:
    title: auto
    author: Author
    series: Optional[Series]

@strawberry.type
class Query:
    books: list[Book] = strawberry_django.field()

schema = strawberry.Schema(
    query=Query
)