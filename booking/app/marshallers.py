from flask_restful import fields


event_fields = {
    'id': fields.String,
    'title': fields.String,
    'ticket_price': fields.Integer,
    'sale_start': fields.String,
    'sale_end': fields.String,
    'max_tickets_in_order': fields.Integer,
    'order_expiration_period': fields.String,
}

order_fields = {
    'id': fields.String,
    'event': fields.String(attribute=lambda order: order.event.id),
    'ticket_holder_name': fields.String,
    'billing_address': fields.String,
    'order_open_time': fields.String,
}