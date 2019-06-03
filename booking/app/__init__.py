from flask import Flask
from flask_restful import Api

from booking.app import views

app = Flask(__name__)
api = Api(app)

api.add_resource(views.EventsListAPI, '/events')
api.add_resource(views.EventDetailAPI, '/event/<string:event_id>')
api.add_resource(views.TicketOrderListAPI, '/order')

