from flask import Flask
from controllers.flight_controller import flight_blueprint
from controllers.booking_controller import booking_blueprint
from controllers.user_controller import user_blueprint  # Import user routes

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(flight_blueprint)
app.register_blueprint(booking_blueprint)
app.register_blueprint(user_blueprint)  # Register user routes

if __name__ == '__main__':
    app.run(debug=True)

