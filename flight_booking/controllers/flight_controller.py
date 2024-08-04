from flask import Blueprint, jsonify
from services.flight_service import FlightService

flight_blueprint = Blueprint('flight', __name__)
flight_service = FlightService()

@flight_blueprint.route('/flights', methods=['GET'])
def get_flights():
    flights = flight_service.get_all_flights()
    return jsonify(flights)

@flight_blueprint.route('/flights/<string:flight_id>', methods=['GET'])
def get_flight(flight_id):
    flight = flight_service.get_flight_by_id(flight_id)
    if flight:
        return jsonify(flight)
    return jsonify({"message": "Flight not found"}), 404
