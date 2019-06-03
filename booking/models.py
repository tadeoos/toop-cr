from datetime import datetime, timedelta
import uuid


class Event:

    def __init__(self, title, total_ticket_count, ticket_price,
                 sale_end, sale_start,
                 max_tickets_in_order=50,
                 order_expiration_period=timedelta(minutes=30)):
        self._id = uuid.uuid4().hex
        self.title = title
        self.total_ticket_count = total_ticket_count
        self.ticket_price = ticket_price
        self.sale_start = sale_start
        self.sale_end = sale_end
        self.max_tickets_in_order = max_tickets_in_order
        self.order_expiration_period = order_expiration_period

    @property
    def id(self):
        return self._id


class TicketOrder:

    def __init__(self, event, ticket_count, ticket_holder_name,
                 billing_address, order_open_time):
        self._id = uuid.uuid4().hex
        self.event = event
        self.ticket_count = ticket_count
        self.status = 0
        # Statuses:
        # 0 - checkout, not paid
        # 1 - paid
        self.ticket_holder_name = ticket_holder_name
        self.billing_address = billing_address
        self.order_open_time = order_open_time

    @property
    def id(self):
        return self._id

    def pay(self):
        self.status == 1

    @property
    def activate(self):
        """When the order is active it decreases the pool of available tickets.

        An order is active when:
        * it's paid
        * it's not paid but the order hasn't expired
        """
        max_order_age = self.event.order_expiration_period
        order_age = datetime.utcnow() - self.order_open_time
        return self.status == 1 or order_age < max_order_age


    @property
    def total(self):
        return self.ticket_count * self.event.ticket_price
