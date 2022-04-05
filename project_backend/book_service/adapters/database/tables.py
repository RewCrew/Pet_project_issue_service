from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    DateTime,
    UniqueConstraint
)

naming_convention = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s'
}

metadata = MetaData(naming_convention=naming_convention)

books = Table(
    'books',
    metadata,
    Column('book_id', Integer, primary_key=True, autoincrement=True),
    Column('book_title', String, nullable=False),
    Column('author_name', String, nullable=False),
    Column('owner_id', Integer, nullable=True)
)


