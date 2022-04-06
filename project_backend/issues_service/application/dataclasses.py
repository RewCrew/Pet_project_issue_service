from typing import Optional

import attr


@attr.dataclass
class Issue:
    action: str
    api: str
    api_id: int
    issue_id: Optional[int] = None


