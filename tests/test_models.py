import pytest

from booking.models import Event, TicketOrder
from datetime import datetime, timedelta


def test_event_id_is_not_mutable():
    event = Event('Rock Live', 50, 229.99,
                  datetime.utcnow() + timedelta(days=1),
                  datetime.utcnow())
    assert event.id is not None
    with pytest.raises(AttributeError):
        event.id = 5


def test_order_id_is_not_mutable():
    order = TicketOrder(None, 5, 'Client Name', 'Somewhere, US',
                        datetime.utcnow())
    assert order.id is not None
    with pytest.raises(AttributeError):
        order.id = 5


def test_order_is_active_when_paid():
    event = Event('Rock Live', 50, 229.99,
                  datetime.utcnow() + timedelta(days=1),
                  datetime.utcnow())

    order = TicketOrder(event, 5, 'Client Name', 'Somewhere, US',
                        datetime.utcnow())
    order.pay()

    assert order.activate is True
