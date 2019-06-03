from booking.storage import get_storage
from booking.models import Event, TicketOrder


class DataManager:

    def __init__(self):
        self._storage = get_storage()

    def can_buy_tickets(self, event_id):
        orders = self._storage.get_orders_for_event(event_id)
        active_orders = filter(lambda order: order.activate, orders)
        tickets_sold = sum(order.ticket_count for order in active_orders)
        total_tickets = self._storage._events.get(event_id).total_ticket_count
        return total_tickets - tickets_sold

    def make(self, event_id, ticket_count, ticket_holder_name,
             billing_address, order_open_time):
        event = self._storage.get(event_id)
        order = TicketOrder(event, ticket_count, ticket_holder_name,
                            billing_address, order_open_time)
        # TODO check availability first!
        self._storage.add_order(order)
        return order

    def pay(self, order_id):
        self._storage.get_order(order_id).pay()

    def list_orders(self, event_id):
        self._storage.get_orders_for_event(event_id)


class ItemManager:

    def __init__(self):
        self._storage = get_storage()

    def create(self, *args, **kwargs):
        event = Event(*args, **kwargs)
        self._storage._events[event.id] = event
        return event

    def list(self):
        return self._storage.get_events()

    def get(self, event_id):
        return self._storage.get_event(event_id)
