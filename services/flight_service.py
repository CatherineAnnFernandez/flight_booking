from models.flight_model import FlightModel

class FlightService:
    def __init__(self):
        self.flight_model = FlightModel()

    def get_all_flights(self):
        flights = self.flight_model.get_all_flights()
        return [
            {
                "flight_id": flight[0], 
                "flight_name": flight[1], 
                "airline": flight[2], 
                "scheduler_no": flight[3],
                "country_code": flight[4],
                "destination": flight[5],
                "departure": flight[6],
                "arrival_time": flight[7],
                "departure_time": flight[8]
            } 
            for flight in flights
        ]

    def get_flight_by_id(self, flight_id):
        flight = self.flight_model.get_flight_by_id(flight_id)
        if flight:
            return {
                "flight_id": flight[0], 
                "flight_name": flight[1], 
                "airline": flight[2], 
                "scheduler_no": flight[3],
                "country_code": flight[4],
                "destination": flight[5],
                "departure": flight[6],
                "arrival_time": flight[7],
                "departure_time": flight[8]
            }
        return None
