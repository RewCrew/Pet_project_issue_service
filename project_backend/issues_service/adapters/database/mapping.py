from sqlalchemy.orm import registry

from issues_service.application import dataclasses

from . import tables

mapper = registry()

mapper.map_imperatively(dataclasses.Issue, tables.issues)

