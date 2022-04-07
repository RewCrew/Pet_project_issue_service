from typing import Optional

import attr


@attr.dataclass
class Book:
    book_title: str
    author_name: str
    owner_id: Optional[int] = None
    book_id: Optional[int] = None
