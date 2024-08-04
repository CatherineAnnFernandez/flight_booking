import mysql.connector
from config import Config

class FlightModel:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB
        )
        self.cursor = self.conn.cursor()

    def get_all_flights(self):
        query = """
        SELECT fd.flight_id, fd.flight_name, fd.airline, st.scheduler_no, st.country_code, st.destination, 
               st.departure, st.arrival_time, st.departure_time 
        FROM flight_details fd 
        JOIN schedule_table st ON fd.flight_id = st.flight_id
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_flight_by_id(self, flight_id):
        query = """
        SELECT fd.flight_id, fd.flight_name, fd.airline, st.scheduler_no, st.country_code, st.destination, 
               st.departure, st.arrival_time, st.departure_time 
        FROM flight_details fd 
        JOIN schedule_table st ON fd.flight_id = st.flight_id 
        WHERE fd.flight_id = %s
        """
        self.cursor.execute(query, (flight_id,))
        return self.cursor.fetchone()
