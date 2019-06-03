
from flask import abort, request
from flask_restful import Resource, marshal_with

from booking.manager import ItemManager, DataManager
from . import marshallers

class EventsListAPI(Resource):

    def __init__(self):
        self.manager = ItemManager()


    @marshal_with(marshallers.event_fields)
    def get(self):
        return self.manager.list()


    @marshal_with(marshallers.event_fields)
    def post(self):
        return self.manager.create(**request.json)

class EventDetailAPI(Resource):

    def __init__(self):
        self.manager = ItemManager()

    @marshal_with(marshallers.event_fields)
    def get(self, event_id):
        try:
            return ItemManager().get(event_id)
        except:
            abort(400)

class TicketOrderListAPI(Resource):

    def __init__(self):
        self.event_manager = ItemManager()
        self.order_manager = DataManager()


    @marshal_with(marshallers.order_fields)
    def get(self):
        return list(self.order_manager._storage._orders.values())


    @marshal_with(marshallers.order_fields)
    def post(self):
        return self.order_manager.make(**request.json)
