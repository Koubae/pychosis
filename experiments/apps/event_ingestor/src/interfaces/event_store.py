from abc import ABC
from typing import Any, TypedDict


class TimeRange(TypedDict, total=False):
    """Optional time range in stats response."""

    earliest: str
    latest: str


class StatsResult(TypedDict, total=False):
    """Aggregated statistics from the event store."""

    total_events: int
    events_by_type: dict[str, int]
    time_range: TimeRange
    ingested_at: str


class ListEventsFilter(TypedDict, total=False):
    """Optional filters for listing events."""

    limit: int
    offset: int
    event_type: str
    since: str
    until: str


class EventLike(ABC):
    """Minimal event shape expected by the store."""

    id: Any
    source: str
    event_type: str
    timestamp: str
    payload: dict[str, Any]


class EventStoreInterface(ABC):
    """Interface for event storage - append, stats, and list."""

    async def append(self, events: list[EventLike]) -> None:
        """Persist one or more events."""
        ...

    async def get_stats(self) -> StatsResult:
        """Return aggregated statistics."""
        ...

    async def list_events(
        self,
        filters: ListEventsFilter | None = None,
    ) -> list[EventLike]:
        """List events with optional filters (pagination, type, time window)."""
        ...
