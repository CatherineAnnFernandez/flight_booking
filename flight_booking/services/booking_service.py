from models.booking_model import BookingModel

class BookingService:
    def __init__(self):
        self.booking_model = BookingModel()

    def create_booking(self, data):
        self.booking_model.create_booking(
            data['flight_id'], 
            data['scheduler_no'], 
            data['passenger_id'], 
            data['booking_no'], 
            data['package_type'], 
            data['class_type'], 
            data['status'], 
            data['remarks']
        )
        return {"message": "Booking successful"}

    def get_bookings_by_user(self, passenger_id):
        bookings = self.booking_model.get_bookings_by_user(passenger_id)
        return [
            {
                "flight_id": booking[0], 
                "scheduler_no": booking[1], 
                "passenger_id": booking[2], 
                "booking_no": booking[3], 
                "package_type": booking[4], 
                "class_type": booking[5], 
                "status": booking[6], 
                "remarks": booking[7]
            } 
            for booking in bookings
        ]

    def get_booking_details(self, booking_no):
        booking = self.booking_model.get_booking_details(booking_no)
        if booking:
            return {
                "flight_id": booking[0], 
                "scheduler_no": booking[1], 
                "passenger_id": booking[2], 
                "booking_no": booking[3], 
                "package_type": booking[4], 
                "class_type": booking[5], 
                "status": booking[6], 
                "remarks": booking[7],
                "first_name": booking[8],
                "last_name": booking[9],
                "email_id": booking[10]
            }
        return None
