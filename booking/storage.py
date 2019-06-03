from flask import app


class StorageError(Exception):
    pass


class TicketStorage:

    def __init__(self):
        self._orders = dict()
        self._events = {}

    def add_event(self, event):
        for event_id in self._events:
            if event.id == event_id:
                raise StorageError(
                    "Event with id '{}' already exists".format(event.id))
        self._events[event.id] = event

    def get_event(self, event_id):
        if event_id in self._events:
            return self._events[event_id]
        else:
            raise StorageError(
                "Event with id '{}' doesn't exist".format(event_id))

    def add_order(self, order):
        if order.event.id not in self._events:
            raise StorageError("Invalid Event id '{}'".format(order.event.id))
        else:
            if order.id in self._orders:
                raise StorageError("Order with id '{}' already exists", order.id)
        self._orders[order.id] = order

    def get_order(self, order_id):
        if order_id in self._orders:
            return self._orders[order_id]
        else:
            raise StorageError(
                "Order with id '{}' doesn't exist".format(order_id))

    def get_orders_for_event(self, event_id):
        a = list()
        for order in self._orders:
            if order.event.id is event_id:
                a.append(order)
        return a

    def get_events(self):
        return list(self._events.values())


def get_storage():
    if not hasattr(app, 'storage'):
        app.storage = TicketStorage()
    return app.storage
