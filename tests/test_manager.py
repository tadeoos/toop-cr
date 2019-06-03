from datetime import datetime, timedelta
import pytest

from booking.app import app

from booking.manager import DataManager, ItemManager
from booking.models import Event


def test_manager_check_can_buy_tickets():
    with app.app_context():
        event = ItemManager().create('Rock Live', 50, 229.99,
                      datetime.utcnow() + timedelta(days=1),
                      datetime.utcnow())
        manager = DataManager()
        can_buy = manager.can_buy_tickets(event.id)

        assert can_buy


def test_manager_list_orders_when_empty():
    with app.app_context():
        event = Event('Rock Live', 50, 229.99,
                      datetime.utcnow() + timedelta(days=1),
                      datetime.utcnow())

        manager = DataManager()
        orders = manager.list_orders(event.id)

        assert not orders
