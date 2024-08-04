import mysql.connector
from config import Config

class BookingModel:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB
        )
        self.cursor = self.conn.cursor()

    def create_booking(self, flight_id, scheduler_no, passenger_id, booking_no, package_type, class_type, status, remarks):
        query = """
        INSERT INTO booking_table (flight_id, scheduler_no, passenger_id, booking_no, package_type, 
                                   class_type, status, remarks) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (flight_id, scheduler_no, passenger_id, booking_no, package_type, class_type, status, remarks))
        self.conn.commit()

    def get_bookings_by_user(self, passenger_id):
        query = """
        SELECT * FROM booking_table WHERE passenger_id = %s
        """
        self.cursor.execute(query, (passenger_id,))
        return self.cursor.fetchall()

    def get_booking_details(self, booking_no):
        query = """
        SELECT bt.*, pd.first_name, pd.last_name, pd.email_id 
        FROM booking_table bt 
        JOIN passenger_details pd ON bt.passenger_id = pd.passenger_id 
        WHERE bt.booking_no = %s
        """
        self.cursor.execute(query, (booking_no,))
        return self.cursor.fetchone()


