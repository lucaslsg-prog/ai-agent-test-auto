from collections.abc import Iterable, Mapping
from dataclasses import dataclass

Ticket = Mapping[str, object]

PRIORITY_ORDER = ("alta", "média", "baixa")


@dataclass
class PrioritizationResult:
    ordered_tickets: list[Ticket]
    unknown_priority_tickets: list[Ticket]


def prioritize_tickets(tickets: Iterable[Ticket]) -> PrioritizationResult:
    """Order known priorities and return unrecognized priorities separately."""
    tickets_by_priority = {priority: [] for priority in PRIORITY_ORDER}
    unknown_priority_tickets = []

    for index, ticket in enumerate(tickets):
        if not isinstance(ticket, Mapping):
            raise ValueError(f"Ticket at index {index} must be a mapping.")

        priority = ticket.get("priority")
        if not isinstance(priority, str):
            raise ValueError(
                f"Ticket at index {index} must have a string 'priority'."
            )

        normalized_priority = priority.strip().casefold()
        if normalized_priority in tickets_by_priority:
            tickets_by_priority[normalized_priority].append(ticket)
        else:
            unknown_priority_tickets.append(ticket)

    ordered_tickets = [
        ticket
        for priority in PRIORITY_ORDER
        for ticket in tickets_by_priority[priority]
    ]
    return PrioritizationResult(
        ordered_tickets=ordered_tickets,
        unknown_priority_tickets=unknown_priority_tickets,
    )
