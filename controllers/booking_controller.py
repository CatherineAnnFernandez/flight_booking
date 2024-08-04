from flask import Blueprint, request, jsonify
from services.booking_service import BookingService

booking_blueprint = Blueprint('booking', __name__)
booking_service = BookingService()

@booking_blueprint.route('/book', methods=['POST'])
def book_flight():
    data = request.json
    response = booking_service.create_booking(data)
    return jsonify(response)

@booking_blueprint.route('/bookings/<string:passenger_id>', methods=['GET'])
def get_user_bookings(passenger_id):
    bookings = booking_service.get_bookings_by_user(passenger_id)
    return jsonify(bookings)

@booking_blueprint.route('/booking/<int:booking_no>', methods=['GET'])
def get_booking_details(booking_no):
    booking = booking_service.get_booking_details(booking_no)
    if booking:
        return jsonify(booking)
    return jsonify({"message": "Booking not found"}), 404
