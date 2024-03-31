from app.application import flask_app
from app.routes import routes_bp
from app.database import create_database
flask_app.register_blueprint(routes_bp)

if __name__ == "__main__":
    create_database()
    flask_app.run(debug=True)  # Set debug=True for development purposes

