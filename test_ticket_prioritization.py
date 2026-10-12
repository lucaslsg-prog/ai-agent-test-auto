import pytest

from ticket_prioritization import prioritize_tickets


def test_orders_priorities_and_preserves_arrival_order_for_ties():
    tickets = [
        {"id": "CH-101", "priority": "baixa"},
        {"id": "CH-102", "priority": "alta"},
        {"id": "CH-103", "priority": "média"},
        {"id": "CH-104", "priority": "ALTA"},
        {"id": "CH-105", "priority": "alta"},
    ]

    result = prioritize_tickets(tickets)

    assert [ticket["id"] for ticket in result.ordered_tickets] == [
        "CH-102",
        "CH-104",
        "CH-105",
        "CH-103",
        "CH-101",
    ]
    assert result.unknown_priority_tickets == []


def test_returns_unknown_priorities_separately_without_losing_arrival_order():
    tickets = [
        {"id": "CH-201", "priority": "urgente"},
        {"id": "CH-202", "priority": "baixa"},
        {"id": "CH-203", "priority": "  "},
    ]

    result = prioritize_tickets(tickets)

    assert [ticket["id"] for ticket in result.ordered_tickets] == ["CH-202"]
    assert [ticket["id"] for ticket in result.unknown_priority_tickets] == [
        "CH-201",
        "CH-203",
    ]


def test_empty_ticket_list_returns_empty_results():
    result = prioritize_tickets([])

    assert result.ordered_tickets == []
    assert result.unknown_priority_tickets == []


@pytest.mark.parametrize(
    "ticket",
    [
        {"id": "CH-301"},
        {"id": "CH-302", "priority": None},
        None,
    ],
)
def test_invalid_ticket_raises_value_error(ticket):
    with pytest.raises(ValueError):
        prioritize_tickets([ticket])
