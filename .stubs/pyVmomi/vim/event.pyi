from datetime import datetime
from typing import List

class Event:
    createdTime: datetime
    key: int
    fullFormattedMessage: str

class EventFilterSpec:
    class ByTime:
        def __init__(self, beginTime: datetime): ...
    time: EventFilterSpec.ByTime

class EventManager:
    latestEvent: Event
    def QueryEvents(self, filer: EventFilterSpec) -> List[Event]: ...
